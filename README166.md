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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f520ee2-750b-36a5-af6f-4a5ecc03a2f3 | -3.50169 | -59.27224 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c63e5894-2b3b-31f5-93b9-8283ee0b442e | -5.9657 | -55.33775 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97439f2f-05ff-3aaf-be63-2c9482dc84e8 | -3.54433 | -54.68567 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 95886e98-32a9-3d85-af24-c7f3ce32ef31 | -2.98987 | -54.06997 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04a11971-85fd-353d-a0c5-cf154542d6c8 | -11.462 | -43.38285 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b022837-ce0c-3a59-afd7-d342ba4d2859 | -11.99886 | -43.46029 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45cc912f-f266-3016-b13d-785b4c17a762 | -2.97793 | -54.03266 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49b3a64c-63c8-3e7d-99f9-d0e0619a0a30 | -6.22323 | -52.88493 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0b54bc1-afb0-326e-ac53-65ab95103d83 | -6.47236 | -55.47913 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6a4a0aa-b760-3325-aef5-fa0f393868a1 | -8.50141 | -54.62341 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f200ca3e-3d52-31e8-9aec-8395a0614628 | -3.73845 | -51.20754 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cc33a1e-f3a4-3a25-a193-63f27a19595c | -3.07373 | -54.2892 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 663b6fdc-056c-32b9-8826-73c3dbbe7619 | -4.14706 | -53.94484 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9675638c-6256-3c30-a37f-78e5f8967b44 | -4.55368 | -54.97728 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46419723-6095-3799-8279-0e85f3e937af | -10.9079 | -45.52146 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2145658c-b69d-3396-b312-62eff0b285aa | -3.25711 | -54.04734 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f631fb42-9041-33f4-94e5-6b936ca5c56c | -2.92614 | -54.19865 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c84c0c8c-dc25-3692-9103-681da45a54a5 | -8.18155 | -54.72034 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f99eca68-f26e-3fd6-b5ef-2916282e4b7b | -8.32431 | -49.12043 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31714f2a-42e6-36ff-887a-1888aaa15153 | -3.53029 | -59.50779 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1ae1057-efc8-3752-9067-5ef0329ccc9f | -8.73826 | -45.13738 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5b2e3c01-5df0-36d9-a765-1103fdb85b2a | -3.56664 | -54.66045 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44cb9482-ea8d-3f00-944e-25e3ab719224 | -3.56906 | -54.48535 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ef69929-f88b-38e8-acfb-4d46ca7bd689 | -6.242 | -52.68112 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73f601b8-127b-30e2-a13f-63b8d23ee13f | -2.3914 | -57.89783 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39cd3e97-4db8-3387-93a0-f53d0c9a2ed2 | -10.57794 | -46.29148 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c208566a-0f37-3957-9f93-d13e59662e28 | -11.26058 | -46.26786 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2bdbdbb-c9aa-3d48-822d-50b4f948d6a2 | -6.16659 | -44.86338 | 2026-10-09 05:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7279014a-c78b-3266-8c96-1868940d8fb4 | -3.10801 | -54.19003 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ddbd4d7-3160-31dd-ad4b-1b183395caa5 | -3.01372 | -54.08074 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| addaf9a5-1ad4-3314-b8b2-9aee4dcf5c44 | -2.87727 | -54.187 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a533dd1a-5e74-39f3-a03a-e2b9d2f686d0 | -5.70632 | -53.48309 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8db584a-a452-3672-9908-40a0f17e6343 | -8.58589 | -53.10515 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50d7a152-b52c-3264-9d45-dafd0adf81de | -3.24038 | -54.66006 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0a4fe89-513d-37f5-ab4c-fd88ae930c2a | -7.18365 | -52.62785 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fc5696b-9f5a-3cd5-912d-c4ee838a1d94 | -6.6786 | -63.0283 | 2026-10-09 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 602ec6c1-ddb4-3875-981f-6dfe78612520 | -8.48999 | -54.6291 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b55dd442-9877-3860-9e54-4f02fba10a4a | -3.60353 | -61.64279 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6b179e4-3a55-3bd3-b814-14d58343aa5f | -3.01628 | -54.21996 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3755308c-09fa-3cba-ad49-c1c4fd4ec7dd | -6.48713 | -55.30245 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eb6a5a6-cd61-3071-896e-92bc07ee6793 | -11.00704 | -47.95927 | 2026-10-09 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d443e2c1-0d47-3cab-9772-acf76c2383e9 | -6.44032 | -55.04271 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46673bfd-b340-3f15-8bce-937433a9a907 | -3.00779 | -54.09256 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21a60eb0-f2f0-34fd-a66f-447509e7e17a | -3.02009 | -54.08568 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24649c1a-4ae9-39bb-915f-c9a4c784ece9 | -2.89508 | -54.07466 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8b3aed-731b-3156-9ca3-091a28762707 | -6.50736 | -55.40119 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3574b26c-baa4-3190-898b-40549e122c48 | -12.02788 | -43.46831 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eef8dff4-a7b5-351b-9cfb-8915e135d6bb | -9.10728 | -48.80175 | 2026-10-09 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 192452bb-dfff-39fd-bb48-a72dcd21ef1c | -3.65107 | -54.06148 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dbe7fc1-1c87-3802-a277-efa3e64dd3be | -7.29588 | -46.1595 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 913a6d16-902c-3ec1-b0fc-2b5eab95d14c | -3.71204 | -59.64526 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78ac9d17-ea1a-3dbe-b7cc-40ae8a9e8014 | -3.25735 | -54.02381 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bb0476b-17e2-36b3-85e4-d529072a1c68 | -5.82405 | -52.04908 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50049b7f-6789-3c7f-bfb7-28bcb90277d3 | -3.91392 | -55.89499 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40cb3b88-40df-3f68-91ce-3563d04474b1 | -11.75684 | -45.47101 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff1d167d-2e45-3056-87a9-74474a5f79ce | -6.45477 | -55.48969 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27026f9a-1292-3af3-a3a7-e47cc7edcec3 | -3.06 | -53.92762 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c71cf17-4857-3116-b9cd-50919727dfeb | -11.46209 | -43.38103 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eedfa844-5acb-391a-83ae-d96d8c3f3572 | -3.22763 | -54.29596 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 91f5c8a5-c436-3cd9-9df8-6654e610eeac | -3.898 | -55.89716 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8bcc7b50-3a4a-308f-af71-8f3c99d3234c | -2.99865 | -53.90313 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a47eff15-f381-34ac-b50f-23c9110cce9e | -3.26329 | -54.00915 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3773aed6-ede9-3d4d-8248-b8e10fcdb5a5 | -3.02507 | -54.05501 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebc634e8-5277-3055-b1ed-c32baeea08ce | -3.09373 | -59.19573 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa0c977f-8507-34ea-9701-6e045e196530 | -9.3445 | -54.50893 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c5ac32a-bd70-31e3-a184-cc1a9486ae6e | -2.39296 | -57.89571 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46d47387-e2ea-380e-ba77-c5148f622b77 | -3.41736 | -54.55114 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19d2b130-e398-3e15-b980-e68342b84dfa | -3.16955 | -58.62347 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6a67439-b7d0-31d2-a824-8699527c7ec1 | -3.7258 | -54.22533 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8088a6b-3a28-33fa-a1ab-f1765248bbe2 | -6.42126 | -55.20188 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bde7bb47-609b-3c75-ad26-21a049774d81 | -3.36332 | -54.74897 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1946e526-0f09-35a8-a3a8-508d1fc5cf80 | -6.92824 | -59.26462 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 429d5eaa-1ee5-32ff-9d6d-79d949d64614 | -2.56721 | -56.16896 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0753b26b-5d42-3d86-ad52-e4b015b62cb6 | -3.16023 | -59.08762 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be650880-e87a-33b8-89b5-0196dad4e587 | -8.66994 | -47.08691 | 2026-10-09 05:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d63a39c6-6dd8-3f78-b1e9-bb84513b3b8d | -3.0791 | -58.08904 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab7f3cf0-00e9-3c18-930e-74cd2b17455e | -2.52107 | -56.61998 | 2026-10-09 05:04:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e30e7426-ae62-379f-81aa-f4438b6aab91 | -4.56053 | -54.95761 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1cecdb-8014-3631-b29c-13db57fb1d2e | -2.56543 | -56.17671 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8e0badb-f919-3cf5-9f56-6cf29b7fd93a | -3.08352 | -58.08979 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d26c167b-7e37-320a-96e0-729295d31f7f | -11.58803 | -43.64938 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bacef1cd-dd9a-3540-aaec-7c1cd1ba6d3d | -5.69909 | -53.47872 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3507f5fa-14a6-3f1d-aae1-430a5c82791f | -9.68969 | -58.09599 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8b0d8f2-6c8c-394f-8349-bd796c873683 | -3.22474 | -54.29157 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3b09a27-d904-38b2-baba-2904a47882c3 | -6.14571 | -47.92525 | 2026-10-09 05:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59e866fc-0320-390b-b820-b6d795f24bec | -12.02379 | -43.45367 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39381a3c-c308-3b76-858c-51618c87371a | -3.1142 | -53.78945 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e62c2260-3e2e-3392-98fc-40853ddd666c | -3.26391 | -54.00536 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43f83bcf-f826-3669-a76b-9364e5540050 | -6.12176 | -55.70235 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19e367ee-296a-3be7-ab6e-7a062444d269 | -4.33048 | -55.01962 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39b140e9-07a6-3c30-9338-233cfedad7e5 | -3.18556 | -58.6405 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 13d57c13-74dc-3d43-a3ee-fa162fcab197 | -3.75933 | -58.51421 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28f8251d-0349-3206-8047-d048ddb0dafc | -8.90626 | -45.21429 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 964c7478-6ae1-321e-88d1-b137f0d47225 | -3.43622 | -56.93864 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71863325-f67b-3fdf-bcbc-0ba205c87cc1 | -4.06918 | -51.04024 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ec12d2f-41c0-3107-bd9d-516a86c05812 | -3.28946 | -54.00163 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e610604a-8e18-39f8-a405-e31ba368310b | -4.54094 | -54.98787 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac200a48-a6c4-37ae-82a9-f57d7bb6c395 | -3.58594 | -54.66616 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a674c2be-503b-3c75-9665-e63b9943a875 | -6.09451 | -53.49791 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34dea87e-c57b-3bcf-a585-10b806515463 | -6.45808 | -55.4692 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README167.md)
