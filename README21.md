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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ab137cd-efb5-342f-a872-b7c3a6f7f073 | -12.46942 | -58.55278 | 2025-06-14 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ca1e5a1-edec-3492-956e-c14a091e1946 | -12.50976 | -58.34491 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb63970f-113f-3514-b35e-8c838e15d546 | -10.92075 | -56.83519 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d67e2fe-2083-3f6c-8ad8-7c603d81572e | -10.92068 | -56.79226 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2b4b023-16ab-3015-82a0-cc57530c4ac8 | -12.27785 | -57.27343 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b06d6104-5032-3601-9218-e0ce76a38236 | -13.90367 | -54.61851 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 02946340-314b-3c2d-bd4b-5d97fc84887d | -11.79922 | -57.35379 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0a8714a-4c8f-350d-9915-71b2b66521f1 | -13.9001 | -54.61799 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0652005a-28ca-35d9-bcb7-a4ff62ba0a5c | -11.79977 | -57.35029 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99d8ae10-9938-3388-aeeb-56953e9c0d7f | -13.72567 | -58.68031 | 2025-06-14 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fb9242b-e46b-3240-a8bb-80e043db06c8 | -16.19576 | -46.46227 | 2025-06-14 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8e9a3648-87d3-3c65-b566-a7eff3be3c87 | -14.67512 | -53.39072 | 2025-06-14 05:06:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 02ef6fbc-46ce-325f-afbc-ab7227352ad9 | -9.88786 | -55.53003 | 2025-06-14 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7368bca4-5a1a-3400-9593-fb8186516ae3 | -10.29196 | -60.55624 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f371d468-8d11-35bb-8006-6740c6f7fe4f | -10.87386 | -54.30984 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0924e7f2-0d28-3976-a91d-1c278ef08b32 | -11.373 | -56.55281 | 2025-06-14 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d398d7aa-fef4-3cfb-844a-c5c60ad8463a | -10.86803 | -54.30083 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c8384ed-cade-3a9c-816c-5586c72ea171 | -10.29567 | -60.55687 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6e3d111-59d4-3487-8644-7a43a9c1da5a | -12.62112 | -57.88131 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b854fab-e457-3be4-a6a4-ab54e8f3aac4 | -12.46888 | -58.4711 | 2025-06-14 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff9682a-06ba-30ce-b256-3a3342280dd7 | -11.1386 | -53.91299 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f99e592-00e5-3fa7-a2a7-aa942ad3f550 | -11.80779 | -56.97058 | 2025-06-14 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d065c4a2-d3d0-3201-a2c4-efc9d45f2ad8 | -10.30012 | -60.55312 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1202a43-e215-3add-bc2e-46282c0943b1 | -10.85916 | -46.70035 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac83b742-8af6-3beb-94be-f4330b68f760 | -10.92129 | -56.8317 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1aa006a-6bf4-30a9-bd36-97abd8c0ed9f | -12.56239 | -57.75951 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b478fb6-5c14-3c47-b772-ec29713c70b9 | -10.36545 | -57.23141 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9ac153f-39b5-3d9e-b8d9-74da7f73b19c | -11.00627 | -55.0867 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6732a273-c5f4-33a0-98cd-1b5481764816 | -10.9334 | -56.84078 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a3c691e4-f308-3ffd-b7d4-2c425094ae10 | -16.20135 | -46.47131 | 2025-06-14 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e700a2f5-e639-3714-8556-04aa599b9e41 | -14.6932 | -53.37331 | 2025-06-14 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e92df40c-9f8d-320c-b8c8-1c2679962a5c | -14.03548 | -55.12495 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 077a8099-52bf-360e-9127-af1111adc89b | -11.80307 | -57.35082 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 415705bd-af4b-3235-a92b-43133f2b1189 | -12.10927 | -48.87468 | 2025-06-14 05:06:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71732981-4517-3f4a-ac6a-19c7b2914b40 | -10.52623 | -47.5871 | 2025-06-14 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a93281a-4190-3cda-b025-f0b4fdb55513 | -13.89481 | -54.60435 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 87168fe2-fd78-324e-84ec-dbc442d32086 | -12.60249 | -47.06609 | 2025-06-14 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15d63a5d-8bfd-39b2-9647-858b44d4cf54 | -10.91799 | -56.83117 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40ef65a2-ea9d-3204-8471-53c5132d799e | -11.87825 | -57.02196 | 2025-06-14 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 361cd02b-211a-327b-9b11-d0965a1a1ac2 | -15.38334 | -47.86566 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f11e28c-d110-3f46-b86c-0106bc813523 | -10.87736 | -54.31038 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 592ef476-d80f-3995-8d91-c3f682cf29c5 | -10.70635 | -46.56006 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95897320-9d75-38ef-a668-69a4da26fca8 | -10.84892 | -46.71173 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf0becb2-89a9-3a22-a1bc-59f9e9f560ad | -16.19522 | -46.47034 | 2025-06-14 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 325a129e-154b-3d92-be64-5dc54d08cf8e | -10.87795 | -54.30642 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d44c44e-6e5b-36c2-aec4-3937075991da | -10.36434 | -57.23841 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06ed5f5-0fab-3302-95ff-75d7ffded474 | -10.91966 | -56.84216 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e9e128b-2928-3922-b44b-7d4cdef09979 | -10.70586 | -46.56409 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aeca0f1-89c1-3440-93b6-9c82371f1c17 | -12.43011 | -54.87177 | 2025-06-14 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5aa5056-13ff-3ad6-b546-2472c140ada1 | -11.57028 | -54.5713 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cacedd86-de8d-3617-925f-487812d98472 | -14.07419 | -53.40489 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e9d4732-023f-3970-a1bf-b39b5036d94e | -12.62331 | -57.88893 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25f995ad-1a31-3d57-bf02-d740056e4db9 | -11.8928 | -47.45941 | 2025-06-14 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a078a96-997b-388a-b24c-46774dce4f70 | -11.07291 | -55.04227 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 913db3b0-cc10-3aae-b9ac-c57486de1c6d | -14.07429 | -53.40829 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae81f984-9cc5-39f2-ae86-e15de1fb6825 | -9.39033 | -57.51971 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9dcd2545-2452-3340-8c2b-17a094c2380b | -12.21244 | -49.64111 | 2025-06-14 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da855b3a-0181-3583-94ab-5eddce6a939e | -12.00066 | -51.61505 | 2025-06-14 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaf61e79-0757-3a87-82c4-1292721fdcfc | -10.86862 | -54.29686 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18f9c40f-53b6-3b24-a760-57e5bdd7f357 | -12.52694 | -57.20266 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36772285-c740-3e57-966a-7bac21e05663 | -10.64871 | -44.48467 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a907d706-ee5f-3e1d-939c-196c5fbec010 | -10.04576 | -64.98495 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79882e0b-6164-3af9-88ec-9aee20662828 | -10.9199 | -54.77705 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d011a6b3-dd32-3f63-a6ff-f9d3add91b53 | -10.92844 | -56.82926 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6518aa7-d058-3d84-a3c7-83b711a99b3a | -14.21778 | -57.3984 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ec5d66d8-36f7-3baf-a38b-1ef3790b38b7 | -14.07251 | -53.39332 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78a70d7d-35af-3388-bac7-571665d1d528 | -11.40646 | -55.08457 | 2025-06-14 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1433c4c-ad66-39a4-8105-645c589587c3 | -10.36875 | -57.23195 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ffa6b2-efe2-3151-8b6b-a1a31333a083 | -13.58684 | -54.28267 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6454050b-e9ef-312b-a409-2751e2e3403a | -11.12958 | -53.94965 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b21660a-5e6a-3dbf-a587-8c755ed58109 | -12.61889 | -57.89545 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36460dbe-e5c5-385a-be53-9080cd46387c | -10.0561 | -59.35743 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52f6450b-2854-3854-ae2e-307164915ad6 | -11.91358 | -57.46929 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d23612ea-cc02-3c07-a8d8-d688fe586a72 | -14.20018 | -57.4028 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72a763cb-1bfa-3698-a053-6c042a364a8b | -14.19632 | -57.4058 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8b54460-021b-3591-8328-e3de1652ce75 | -10.04522 | -64.98784 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e53da74-33c7-3e2b-956b-49d512f9c8fe | -10.8503 | -53.78442 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2436691-7846-350c-b3a2-df91104ee8d4 | -11.01001 | -55.0902 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c426d98-636e-3cf0-8a05-8dbf2fb389f2 | -15.99616 | -49.81869 | 2025-06-14 05:06:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d147c6cc-9e2b-3101-9475-e96e93191ec4 | -14.20513 | -57.41449 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d375755-bc1f-3477-a118-ea98ddd85829 | -13.90001 | -54.64349 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b1509ae-9eb7-3d38-baaa-0ffb642ada52 | -11.99652 | -51.6144 | 2025-06-14 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddd6c2a3-1c19-39ec-9a51-88cc668bf9b0 | -14.22054 | -57.40248 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 796b96b3-343c-39de-948c-569feb86525c | -10.93616 | -56.8448 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 59dc7397-7961-33e0-ae6b-4ae2b345210d | -11.81352 | -57.34892 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400f8f77-119c-3764-98c9-2c1a43f780ac | -10.92514 | -56.82874 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00edadc2-e5d2-326a-83ea-d79c791c0920 | -10.36489 | -57.23491 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f45d188c-0068-36ed-a9d9-9553b2321a2b | -10.92333 | -54.7776 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7037e536-2bf8-364c-8bc1-200d0df13d81 | -11.88045 | -54.67635 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6afac904-bf2a-35ea-b96a-e3149dd093c7 | -13.90062 | -54.63934 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d9bf6df-30b9-3d55-ac23-a6cff28b3dfb | -10.83083 | -56.95239 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2e45bbf-bb0c-38f5-9543-ebdfefbfd5cd | -13.90088 | -54.60764 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 966a951f-1024-3534-9110-a5e5f56f8bda | -14.07168 | -53.3947 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73f20e4f-fcd2-33a4-9fac-19613c4cf47d | -10.56506 | -52.01214 | 2025-06-14 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18780e23-8699-3cc2-8ce3-c1efd7e92380 | -10.26326 | -54.99685 | 2025-06-14 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1113d2d8-12c3-3eca-bbc8-bc3e5f15094b | -9.91854 | -59.91003 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c206071-4419-31b3-a497-2c929ee9b3c1 | -12.603 | -47.06178 | 2025-06-14 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54db3acd-adf3-373f-949e-598ea6b4f358 | -11.91413 | -57.46577 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99d166b6-5ba4-3fec-b042-79a39d65d0c5 | -14.20953 | -57.40796 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ba89ddf1-77e6-373f-918b-30d4ce997cd8 | -11.00967 | -55.08722 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README22.md)
