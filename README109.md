# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e678d774-8212-38cf-8662-2441f432ea98 | -2.98967 | -54.08352 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 9079ee34-5750-3770-a441-3853ce0dd658 | -5.75388 | -42.05165 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4bad0894-1c15-33cb-be7e-0e72bcc96037 | -3.31248 | -54.05859 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b96e4e2-bdef-3e74-8dfd-b2d0390f4ba6 | -3.00263 | -54.04977 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78444e5d-7716-3195-ab51-76e32c199560 | -2.39826 | -57.88726 | 2026-10-08 04:46:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a72a4fc-3517-3088-9e77-7ce6415387cd | -3.01229 | -54.06019 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b38ea741-049e-31a9-9d3b-5c1f880e6756 | -3.55123 | -50.09752 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 746441e8-969a-35c4-8e68-1a452b6179f6 | -2.58562 | -56.15865 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8966997-38eb-32b3-98b2-8af6691e0fcd | -3.73568 | -51.20686 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f5383b8-5ae6-3f98-a0ac-84bf50ce026c | -3.10528 | -53.76256 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7344f492-4b4c-3bb2-9e58-43d3245c5f61 | -3.3037 | -54.66676 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45715568-e888-3660-89a0-a2d204ba8934 | -3.07411 | -53.95461 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3b99e1a6-5cdf-390e-b3e4-81ff1a880b76 | -2.96741 | -54.17491 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4f1ab13-c946-323a-ae60-2d0685a6a83b | -10.43605 | -47.28266 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| aa2d6340-66b5-3601-b0f5-9f12a31f836e | -11.45598 | -43.38562 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09c51236-cddc-35db-950e-520f0ccceb00 | -3.63477 | -59.56748 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17cc629c-0885-34ba-8519-fa0849b8cb8d | -2.93467 | -54.1424 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 223f51c2-1570-31dc-a208-89abc01a5557 | -3.10262 | -54.27127 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 603fa343-e318-3bf6-9f49-2d1c5cdbdb7b | -6.15136 | -47.9269 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b117592d-2b84-3973-8e2c-69ceed416489 | -4.92195 | -55.85644 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54ad53bf-502d-3a37-8563-4e4e1357600b | -2.93464 | -54.05431 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f581a11-f43d-324e-bbda-659803e08282 | -2.39086 | -56.12909 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 656fec4c-8922-37cb-a256-92ef6ca6a6e5 | -3.16275 | -54.72607 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c7ef13f-0c38-396e-9565-a3d76912f12a | -3.59472 | -54.57191 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cff66e1a-1d6e-31dd-afa3-6df1398ea772 | -4.06687 | -59.84875 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4d21a1f-e981-3619-aa24-38e8268672d3 | -4.15531 | -55.14438 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5ca80d5-1de9-3d2d-951a-30e52361026f | -6.09562 | -49.40686 | 2026-10-08 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f5732876-e4ff-30f5-8526-5c549d6d78c3 | -7.73302 | -45.44391 | 2026-10-08 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48c768f3-07ef-3176-ac60-cac6c35e25f6 | -3.58648 | -54.57523 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 495dbf19-e20d-3eec-85bd-169fedc2f530 | -4.03982 | -54.2254 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85a52779-4aee-30f7-a319-076a67202306 | -3.11252 | -53.76369 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 946dc8e1-7b50-3864-90ad-430955c55d6b | -3.0655 | -54.17018 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 301d592a-8237-3025-bcbf-6a9d69e22093 | -8.71873 | -45.18598 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2d06cc96-f9a4-3bd6-8c53-bde7f18c7848 | -2.50915 | -56.17489 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6e406a0-0e87-3e98-9a19-d7ae746b61f3 | -6.23951 | -52.84957 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9107a9ca-b3e4-305b-89f2-5f6df239f9bd | -11.63783 | -43.59548 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e75caad-ea2e-3270-aa88-c42aabde4af8 | -3.57164 | -59.45931 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 799f9a40-a4a9-34fc-85b9-081389138cc2 | -2.48839 | -56.14318 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 64e2adb0-48c6-332d-9f98-be8d9673469d | -3.10833 | -54.16346 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 36731fe8-27fa-3d57-9e57-12fb95d3e1e8 | -2.99686 | -54.06226 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aafd955d-9d57-318b-96ba-7ea4775cdef0 | -2.78563 | -57.64682 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eea33d94-e252-3798-b412-b74c241393cd | -5.20333 | -48.21014 | 2026-10-08 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e2467a7-13fd-3b85-9a1f-06e6ff701fec | -3.22543 | -54.3034 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 220ff0f0-5c8f-3761-bb55-5029e057be31 | -5.82583 | -52.04625 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b57a1a1-4a77-33bf-9b4e-85865b4c4cca | -3.77866 | -59.25584 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca8a4057-2616-38ec-bfff-b5430324d0b3 | -3.02306 | -53.89843 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 159b690b-a58b-37e6-873e-60e4eeb38c4e | -3.28095 | -54.04626 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5728505c-01f8-3ff8-a8a0-80eac1699ba0 | -2.98916 | -54.11034 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 49f1b0af-4e77-338d-9321-1adda2370fe0 | -7.39358 | -55.20409 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ac37572-2035-3cf6-a397-33f45d55043e | -3.30969 | -53.86263 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0edfde3e-0395-3db8-b8dc-20441548154c | -7.34328 | -45.28539 | 2026-10-08 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d18313da-25c5-37af-a24a-88ca054e16df | -3.29665 | -61.01681 | 2026-10-08 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8c1c2161-43bd-309d-8c04-37917b204af3 | -5.6868 | -53.49094 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5208d5ac-b4a6-3313-a937-d41f223c82ed | -2.94418 | -54.11414 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f37b0867-2059-3572-8726-bdb35e54e728 | -3.29413 | -54.05575 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8d67d4e-b552-35fb-a123-8f26dbb506aa | -3.72039 | -54.22832 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6937c6de-eebd-37cc-922b-d8e8cfb326c6 | -7.88138 | -55.0003 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9f52316-9073-3865-ac91-511dc5e5a0fc | -3.47654 | -54.63077 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b52e2ac-a69b-3283-a41e-4e9a206c07a0 | -2.92967 | -54.20699 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15107215-15b4-3bf1-b71b-56610dc9f33f | -3.27021 | -54.06678 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b647eb17-a0e0-3ad2-a886-e03a94b116e2 | -7.87534 | -54.96857 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51c73fbc-dd2f-38a1-903e-ff4e26761f7f | -9.91327 | -46.79475 | 2026-10-08 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f39b622-7801-36ee-b4a2-c6847c9a1953 | -6.15412 | -52.65838 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c93e4835-6038-3c94-bfe5-1e64ad59f3fb | -3.28663 | -54.03393 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffb49f8a-ae84-31e3-a7c2-b5ce7ed9c598 | -4.93824 | -55.80627 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfbb2eb8-a2ee-35f9-9ffc-24085726be16 | -5.96911 | -55.35837 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a684d53c-54b5-368f-aed8-8647df10ea78 | -2.7823 | -54.06723 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b44f1b8e-92cf-3814-9fb9-8568994d2a98 | -3.40952 | -58.90973 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dde27c47-12b0-3fe7-b2cd-f6f646555b4c | -3.07052 | -54.25722 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6e5731e-2678-351e-bd38-614dbf6db3ad | -2.78041 | -56.50525 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6590b60-7de3-3daf-abe8-c32e8d4f5798 | -7.18462 | -52.62409 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 813e079b-138c-3a26-a822-6941c03c4df2 | -3.02033 | -53.91553 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40fc0a62-2d11-3b83-8c49-80677e5b33c0 | -3.05282 | -53.94688 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c38b6bed-4494-3b9c-8af2-c97628b35e1e | -3.66764 | -60.62354 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4a2d915-77f1-35f5-8590-f703bc0b96aa | -7.40605 | -55.15141 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f4dfcc9-86ef-38c0-b16f-b93e4af2c568 | -3.6567 | -50.94701 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a57b44c-e5bf-3838-94b5-b3af1473ffaa | -3.21635 | -53.88723 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c2ad38f-5935-3beb-ba58-0a399d168ddd | -7.08376 | -52.68129 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3e27c1-5c78-3aa8-843c-1116dd73d5df | -2.48714 | -56.15104 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1e709ba-2744-3a5e-8667-20e01a3ef5be | -6.48344 | -55.30239 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2664d8a-2116-3bc9-8ec2-7ed567e471ae | -3.11704 | -53.78162 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5207aa8d-d7a8-387f-9942-7f8a10ace790 | -8.08064 | -55.29904 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2866ce4c-0a2b-3e59-a03d-4af035c8c4b9 | -3.17125 | -54.73947 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17fca46a-30f7-3d91-90a4-db9fd3ad9672 | -11.46166 | -43.38512 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f15663df-16db-357e-9917-e37074a0b83f | -3.05653 | -54.15525 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21e6a542-d3ff-3e45-8372-b92dc4d4f003 | -9.89853 | -44.80811 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 12ab6786-48d9-3fa9-a0e1-cae725b3a958 | -6.09005 | -53.49405 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42d84021-fd4b-3c2f-a833-c6bb66d3fbbe | -9.68918 | -58.09718 | 2026-10-08 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9f44f0e-cc30-306e-8532-2d6968092ee4 | -3.52483 | -54.66912 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f81bcf6a-66aa-31e3-b4a7-6e1235edd3dd | -8.08339 | -55.29776 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f49fdcb0-bee5-383a-a6ea-554791d92b8c | -7.21026 | -45.35392 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc2ff1e1-02fa-3781-80b5-774a0c3d17ee | -3.87591 | -55.99527 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87798a84-211f-305f-a604-7a9943e3c047 | -2.47054 | -56.09203 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d0d2054-7ff7-3c09-bfc1-d8bdfcfd20f6 | -8.25288 | -54.7252 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce572c0c-c17b-393e-b493-f1d56842e712 | -7.87604 | -54.96431 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44ce833c-232f-3ccd-8723-4b52652e04dc | -3.01272 | -54.10505 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 515710f1-8e18-35c8-8c16-5d9f65711505 | -2.48071 | -56.10967 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adb2d0d7-fa73-34be-a6f7-2e071e027d2a | -3.84345 | -55.91422 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65e2fdb2-3154-319a-aa30-5a9b6ab1cdcb | -5.75293 | -42.05822 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bb361264-35f4-335a-bb7a-c14ed7474e2e | -8.21454 | -46.36963 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README110.md)
