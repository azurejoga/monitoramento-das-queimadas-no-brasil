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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7d3338e-c9e3-3b9b-be8a-be525c670f57 | -3.5379 | -54.633301 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1961cc72-4261-31f8-b55a-bb6089681fd2 | -2.8424 | -54.112 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed9d0e2-6f85-3c08-b6ea-2b30af48e5b4 | -3.3017 | -54.0457 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce7864e-7212-3078-9b16-153b0ba3ed74 | -2.4816 | -56.1189 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24261684-8046-3780-bdb8-bcddd2364a4c | -2.7228 | -57.468102 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d27ea80-6d94-35f1-a0a6-3ce6769a19e2 | -3.2118 | -53.876499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21554b34-467f-3391-924a-42efc64b4048 | -2.5613 | -56.1525 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7a3b1c-b9a4-3542-9b4a-040f563b586e | -2.0564 | -56.381599 | 2026-10-08 00:26:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ecea20d-f46c-32c0-b01c-8e96f561354e | -4.2467 | -50.744301 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e09709-25ef-3ca4-b7ff-66a2fd1f55ea | -3.3548 | -59.890701 | 2026-10-08 00:26:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d71c72f-aa9e-3cf5-b7b0-f583c880358e | -3.043 | -53.950802 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3b4672-b460-364d-a0cd-d23c22fff91f | -16.8519 | -40.589401 | 2026-10-08 00:26:00 | METOP-B | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0b4d0cb-208e-3dd5-a45d-f73bc9de230c | -9.5898 | -47.782799 | 2026-10-08 00:26:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 094af2e1-68ed-3bc3-b09b-d7896e24fdf1 | -13.4955 | -44.351898 | 2026-10-08 00:26:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 881cb44e-c044-301a-b8d8-18e1ed5d15fc | -4.5789 | -54.952999 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6862cc7d-e28d-3ec5-8964-d5ccaa337cf2 | -1.1083 | -54.1479 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54228043-6f6c-3224-ab88-bd67287f39ca | -2.99 | -54.0354 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7805e0b-7b44-3934-b2e1-6dbcafe6d706 | -3.5376 | -59.464901 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 094366ae-0b4d-35cf-a36c-b283f8dbfef9 | -1.8263 | -55.0425 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd26ff6f-c3b5-3073-9c2f-079bcba17f96 | -2.9589 | -54.2164 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66846130-585e-33b1-9f6a-1f5551f4634e | -3.0606 | -54.1647 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 533eb49b-ea7b-3c5a-9aab-0115901555fe | 1.6903 | -55.6301 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e679c5fb-cbcc-3c4f-b629-08cd3ee0f3bd | -3.2992 | -54.6721 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2029f6-407c-3bf5-9370-52ac7f0b52a0 | -3.4811 | -54.610199 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0df06cc-55b0-31bd-be5d-6aa8ef3def5f | -2.826 | -54.130199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63db24e8-569c-3b14-ba5a-dd7a4f7ead81 | -6.6185 | -59.925598 | 2026-10-08 00:26:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6f99c52-7dfc-33e1-8db4-c54844bae61f | -2.8052 | -54.0839 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22a6c6d6-5e05-373f-a2a8-9a3081183766 | -3.0017 | -54.177799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 801aeb4e-4eb7-347d-90a8-2e2ecd22406a | -9.8843 | -50.498501 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8ede4a6-be09-35f9-b31c-b4a5e3a34553 | -6.212 | -52.831799 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf793ac-08e0-332d-83f5-9c4925cd3710 | -3.3083 | -54.029701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455993da-3a55-3a3a-bafe-43c0cf3f9f63 | -3.2692 | -51.062099 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5c8e2a-5876-3e14-bb84-4dc4fd76755d | -4.4178 | -55.7495 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d14aaf21-6bf8-3b52-bba0-36676922cb34 | -2.8911 | -54.1446 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a666242-1b47-3063-9e96-2a60ed43b801 | -5.7384 | -45.166401 | 2026-10-08 00:26:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78905418-b7ce-3645-886f-86e70479db45 | -3.9725 | -56.1064 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d8f506e-1d7e-3076-b83d-d125bc07df85 | -3.4728 | -54.619099 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8bbf35e-2648-322b-91a7-d37cc16f5b7d | -3.7369 | -51.214199 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd49bfbf-62c4-3d18-9513-6624d2f69347 | -2.045 | -56.1936 | 2026-10-08 00:26:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da285156-90a2-31d7-a30c-c339e7af1035 | -1.4997 | -54.828999 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a38fea69-cf47-3a61-8452-9ef8012101d0 | -3.8499 | -51.929001 | 2026-10-08 00:26:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74babc83-06dd-30fc-ad0b-316c1aad32f2 | -3.1067 | -54.277199 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5044a46-33c9-3bb6-8a08-9bfec367c39b | -2.8244 | -54.123299 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e89d246c-763e-3233-8c44-932a9ea80aba | -3.5167 | -54.630901 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 312a940c-bc83-385e-bffa-2337de8ecbbc | -1.4759 | -54.633202 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fddffbc1-27e3-3102-8726-f2c449fc719d | -2.9881 | -54.072201 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 414c3cec-91e5-35ec-94b4-a760981e038f | -2.4409 | -56.533699 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6032f2-12c3-3f89-82d3-16ca52e8d78e | -3.465 | -59.5541 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2611d222-cbf5-3b4a-8c5f-56c98d656be2 | -2.5039 | -56.172501 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf4184d6-a9ed-355d-9cac-4254d2b0e589 | -3.554 | -59.492699 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0000ee-a9d2-3b92-a2af-065240e792dd | -1.1832 | -55.663601 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e08cc1-38bf-3a94-901f-26fd933cde7f | -3.0557 | -57.483898 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 143ac313-5787-38d5-adf5-7593dd83144c | -5.2953 | -60.096802 | 2026-10-08 00:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d459674-f604-39fd-a4e7-1268702a347a | -3.3644 | -58.175701 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91a1cd0f-32de-3f66-991e-3c50bf1d4191 | -1.8312 | -54.9272 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79f7a609-fc8a-3eec-9d1e-237d7359b427 | -4.8183 | -54.734798 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a285e15-78f1-3d08-ada1-fea753237f30 | -7.9027 | -54.706299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7a45bc1-a9ee-310c-8f9c-b7374aa008a7 | -2.8822 | -54.879299 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c78123ae-49f6-3d40-8865-714da19b8200 | -3.1114 | -53.752399 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2690a6-78d2-3f66-b7d1-3946a79011d1 | -2.5055 | -56.179501 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a509c889-7404-3da5-a114-9cae25fd2856 | 2.0014 | -61.412201 | 2026-10-08 00:26:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 14883265-3875-33ee-8c07-f2edf5af2431 | -3.1297 | -53.696701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02a035a4-637b-3ed9-8970-02b7dd409ca6 | -2.7608 | -54.115601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d38931c-4755-3b3a-923d-34053ae40428 | -1.1847 | -55.670399 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f57dee2-25c7-37c2-abb6-b5926fcc4a50 | -2.8932 | -56.666801 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49d9a4fc-f93a-3be2-ae76-15fb706c195b | -6.2022 | -52.834 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0630aa3-3238-3740-8939-74267a8de02b | -3.6664 | -57.085098 | 2026-10-08 00:26:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc43d7d9-1ac0-3ff8-98ab-5a9c78b3bb5f | -14.91 | -48.109001 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 87e3e97c-2d75-3f4a-bbf4-f42a6d171168 | -2.8487 | -54.139599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a89b71a-d71c-394b-9086-2e4151a9c88d | -2.5809 | -56.148201 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3c9f257-831b-39eb-94da-1b356cea4a94 | -3.0733 | -59.269402 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd3e1ca-9dc7-3501-839b-4d8b95ff2237 | -2.8376 | -57.475101 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13c5bdb5-e79d-300a-ae89-7d9aae229814 | -3.1956 | -50.5648 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 449103c0-ab8c-3733-856c-8ac0fcc0d097 | -3.0158 | -54.239799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6dea9f9-adca-3b11-830a-40089f551b61 | -14.9295 | -48.104 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1c6e9c3-9f9c-3c6f-ae06-19be96eac7a2 | -8.2492 | -54.6437 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6cd67a6-5fbe-3417-bb26-048bd7027ea2 | -8.2902 | -50.259399 | 2026-10-08 00:26:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e4cff31-1788-37ff-8644-2776dba7b19f | -4.0653 | -51.029301 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c048d6f-88e1-3f12-88b5-20ea7d3739d4 | 4.0951 | -60.550701 | 2026-10-08 00:26:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 212b86d1-553e-3ee8-87fd-294734271b58 | -3.053 | -54.267601 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78dc3459-b70e-3384-b376-6bb2f4d7157d | -10.8886 | -49.148701 | 2026-10-08 00:26:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a77cf2a-f860-3eb3-a095-a5023395c9b9 | -11.7714 | -46.777802 | 2026-10-08 00:26:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c8f22c0-c3cb-3cb4-ae07-0846d1fa2b67 | -3.0258 | -54.0564 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74708b1b-cb0f-33e0-97ee-2ca5336e0ff3 | -3.5675 | -54.4907 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d810d3-03c3-3d7b-8839-bddc6effa7f0 | -2.9386 | -54.126801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bba53f09-0d25-3bda-84de-05e81f3540f8 | -5.9657 | -55.348499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 851d1697-0095-3bcb-ac9c-9ad518586b65 | -6.1483 | -52.643101 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfeee6c6-0543-3d82-accc-8d0e61f2c688 | -2.9919 | -54.18 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 722919cc-6873-3444-aa05-e68dbeeaae93 | -3.0124 | -54.088501 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057120b5-3563-3f1e-b683-ee5181f5fd51 | -3.0559 | -54.1441 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1d79296-0a6d-3999-80bc-01196010f11d | -3.5796 | -54.681301 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7009a0ee-1c7e-3cc0-8442-b679671aea15 | -1.5213 | -54.5149 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335fd57f-b638-34b9-9117-28d6ee80a733 | -3.1836 | -50.557499 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50eaa9a9-c421-36e1-b0ac-e24d19b782aa | -7.1966 | -45.334202 | 2026-10-08 00:26:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c50c231d-3d86-3734-972b-092d0dd28e84 | -2.7938 | -54.079201 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa6588a-983b-3c70-8d3f-16bc9b5db7dc | -3.0026 | -54.090698 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ba44fa-33e8-3af1-b5a5-d4cb14786364 | -6.3913 | -55.224899 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15625482-82dc-37ff-8be2-1c31c824aac1 | -3.1787 | -50.447201 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ebce286-5ae7-35ce-ba28-90f94718d2bc | -3.1697 | -53.8274 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 393037ca-25fc-3774-8fc1-4731b323b963 | -2.5083 | -56.237598 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
