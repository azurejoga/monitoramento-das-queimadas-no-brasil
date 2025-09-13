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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47b073d5-692e-3c42-88b2-94796b7ba19e | -11.17818 | -55.08421 | 2025-09-13 04:08:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce8ca6af-7451-3a37-ae75-ebf2536109d5 | -14.41909 | -46.40411 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3620d72-6ea3-3a05-a22f-8e11a74291ff | -14.43601 | -48.43739 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eba1917d-8934-3274-bbe0-39f80e26a82d | -10.65488 | -46.28257 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c0dd10b-9400-3ffd-8d81-cad567f17cf6 | -13.29818 | -43.7624 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06c884fa-1bab-3634-9baa-74663c2610b1 | -9.71602 | -48.31844 | 2025-09-13 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 977a4e69-4f56-38c0-befb-ea462b4bf5b1 | -14.29518 | -46.0653 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7bce5ee1-5e02-330f-bb32-a8d5c8af31bc | -9.02844 | -47.05451 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11d7aa92-3262-3437-b0f5-433037dbfacc | -9.90734 | -51.89673 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d807bf2-978c-3fe8-9571-04242db0bb18 | -14.18547 | -46.26083 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f9550ad5-fa5f-3561-8441-605db9a3ee4a | -11.83974 | -50.56298 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 9a684e4f-2ee4-3666-8986-1780a3467c72 | -9.06311 | -47.03099 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c6cd285b-6068-3aec-99c7-edfe6a9e54fa | -12.08125 | -47.57734 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f1eac50-5f1c-3a0c-8381-783ad9773baa | -11.39622 | -43.52549 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41b524e7-5345-39c7-9103-d28a43ecbf2f | -12.94794 | -48.00787 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f44de90-b739-3979-bff7-5997599122ff | -15.06377 | -48.01118 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15bdffe7-424e-3976-be91-8a7ead788c38 | -10.51053 | -51.5404 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 746f769b-6472-374d-899b-59177bb14d13 | -11.45588 | -43.57477 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ad937a-f038-3967-bb40-0eaddd3e7b85 | -7.97054 | -55.30752 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2876e475-7017-3360-8196-3096368ed232 | -13.26155 | -51.70928 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0c4893a-d805-38b7-b8e1-e6f0c4bf9d28 | -10.77365 | -50.54922 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0349840-dc55-36c6-8a9c-b76fbd312c50 | -11.42508 | -45.62194 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b0d3d0f-cbda-30db-97e7-7099d646bd58 | -12.83384 | -47.94548 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f218869c-a9ee-3b52-9435-485c761f2282 | -10.50772 | -51.52925 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e995f69-20a4-3ed4-a84e-3f6eed438393 | -9.73432 | -48.09101 | 2025-09-13 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 996fd6fb-580a-31dd-8052-c256bd962b90 | -7.91088 | -45.22687 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 790d9969-78ba-3e1d-bc61-3dc5ed70f852 | -11.72355 | -46.58227 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8f4838a-28cd-3bc6-ba2d-045ead4c15a4 | -9.82578 | -48.89743 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44d47253-689e-32f3-a2ef-de7a16346446 | -11.07074 | -40.80536 | 2025-09-13 04:08:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3a246fd-3657-39e0-8a7e-1a30c8b9bb3a | -9.97196 | -50.30349 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 86f811cc-6707-3d8e-8b79-b4d56801bc03 | -11.76806 | -50.5531 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fb4e22cf-31ca-3430-b759-8cc3db4f6dc5 | -12.99473 | -46.75006 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c4a5a38-1215-382f-b193-293ee3453165 | -12.12788 | -44.82535 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 642eb306-3a1b-3e6e-ab6d-20ae25911228 | -11.37909 | -43.50444 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04a52fac-85ec-338c-aa52-f1653fe6bb14 | -13.26423 | -43.76388 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b82ba75-29f3-3823-97bf-544b09f94a91 | -11.812 | -46.74322 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a49a3a-7760-3d14-929f-8937500f6800 | -8.10241 | -50.18969 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 701e0403-fc83-3a4d-a8ff-da2ba92e0fd5 | -12.10804 | -44.88557 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dad3d215-5d23-398f-9cbc-7df2bd370ad5 | -12.94528 | -47.99961 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dcbb38da-b4ba-317e-b4ca-e5489a295fff | -9.71424 | -46.87285 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c38720be-53e1-34dd-91d9-babf862b762b | -14.21314 | -46.2705 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8832c4a-3074-347c-ba64-6dda07d5afe4 | -9.69392 | -47.5405 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 765e34a0-6a47-3a3d-84ab-c06c16d91f20 | -12.85155 | -47.93813 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d16db5b4-b4dc-3aa4-9575-99d8f87ade17 | -11.82916 | -50.56643 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f3f8f8e-b1f5-3cd5-b806-51883f2f06d0 | -14.18406 | -46.26905 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8bb6fd6a-e37c-31d3-9792-3adeb1b14b44 | -12.85246 | -47.93297 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 398eeab1-83c2-3b37-a9bc-cfeda479dce4 | -12.99335 | -46.73564 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4497f102-e92e-3b4e-9e17-c98544cd6e10 | -13.26707 | -43.74607 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4ca003f-d317-3ff7-854b-4612f045e1ec | -14.05531 | -44.31216 | 2025-09-13 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1beca1d-42ad-358d-a434-27661ed21c4c | -9.02877 | -47.03963 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| eb28a231-edbe-3f2b-877d-5fa6e31d33e9 | -12.08097 | -47.57383 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 971cfea8-764d-38b2-b15e-3d5deea068ee | -12.81976 | -47.93229 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 715a418c-b6bd-385c-b026-7bffba0c9d16 | -11.41065 | -43.6487 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48b7d76e-c1df-3a61-8b3a-eb1dfe536b6a | -13.13589 | -47.13171 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 319100bc-ace9-30f7-ae6a-46dc7acb6118 | -9.19456 | -45.77905 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90347caf-3276-31d7-9596-1d31a6837ebd | -12.56691 | -44.67422 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62f9e177-de35-3f73-a4c8-e0b55b578994 | -12.09521 | -44.89925 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f10558c-fceb-335e-bd67-ef3a02d5ca36 | -12.94332 | -48.01075 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d98f417e-9220-3b8c-9357-5e53e6b0cf7e | -11.4691 | -43.59889 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62dc06ff-b388-33a2-ba64-910e00378f0e | -11.37851 | -43.50799 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 622d238f-0fcd-376f-9009-0b83be7f2479 | -11.43392 | -43.54632 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f41c872-00cf-378e-988b-7679acec15f6 | -8.92242 | -46.15194 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0ab27aa-0c3b-3d99-94a3-b672f8346aed | -10.22771 | -48.62029 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba211c5f-2b20-302f-b6ee-98a94d5f03a7 | -14.43265 | -46.41101 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26ceaac3-314d-3f61-a043-574c00b47e90 | -10.71214 | -48.61269 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 920fb001-946c-3cca-afb4-0063ce68b5ed | -13.00269 | -44.11771 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 300ece5f-f62a-3587-a1af-b0f6276cf5ce | -13.15017 | -47.13921 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee4018f5-9163-358b-8dae-e93aa1d64451 | -11.18694 | -51.42924 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| af81caf0-4906-3412-8930-3b106e9dc073 | -13.17657 | -47.27806 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc8cda9e-a7a4-32a5-822d-85fa9a1a9b87 | -14.68631 | -43.6647 | 2025-09-13 04:08:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8137375-5f99-34a0-8021-2e572223d5d9 | -13.29372 | -43.76897 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71226680-d4eb-35b6-a7e7-0925a7a2f8c0 | -14.43671 | -47.31931 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7701c7eb-41e9-37bd-80ac-724a7e17274a | -14.19186 | -46.2877 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d87cb798-8dd9-36b9-8c37-7e04e4fceed5 | -11.46082 | -43.58654 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b28d5df-7138-37bb-a458-fdbc99a86187 | -11.17954 | -51.43221 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8de7ebaf-7f6e-38be-b803-589b8440ee42 | -11.10695 | -51.42109 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66d6d9dc-67fa-35a0-a66e-066a64bb00f9 | -13.35202 | -44.44147 | 2025-09-13 04:08:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f70affec-8998-3957-94af-0e473fdebb11 | -11.76676 | -50.55423 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f383ff98-a1ce-3ffb-a833-e3f01271c0e7 | -10.79309 | -45.9949 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5178f167-ba43-328a-be3f-46b18a91c948 | -12.12062 | -44.84775 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b246647-52e6-399c-a6af-3bc1d9bc1920 | -12.10758 | -47.584 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51ca4a27-fa08-333a-a1de-03e76051fb5f | -13.23878 | -43.7523 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4955b2be-c840-3fd3-a06a-c154b9ccbbc5 | -9.81775 | -48.89099 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fadf07f-8616-37e0-8461-bb7592f3aa3f | -13.58087 | -44.88971 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7842fd45-79f3-3dc8-bd05-9593b29d95f9 | -13.17283 | -47.27699 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 257a2876-2c62-31aa-87d3-e9f13c3d3687 | -10.45495 | -50.60586 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2844258e-ee62-3cff-a43c-924fb8f33bbd | -9.24488 | -51.25559 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c24cae6-55d3-3e14-849f-6c88cf228c37 | -11.92943 | -51.13643 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24f07817-be50-3d6f-8b05-329632459c6e | -13.00162 | -46.74459 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9629901a-8c73-3f80-8c2a-b9092a0cad3c | -12.1021 | -44.85711 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1e57988-b38a-3883-bab0-089dd0d4cbbf | -12.94855 | -48.00437 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 63cc2ef5-f81a-3472-b981-eac557a5246a | -11.73945 | -46.62373 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9291c40-0542-3dd9-b87a-88a49cf4a0e9 | -10.50201 | -51.53079 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfe4cc76-37c8-3ee3-bb93-252a4167477a | -10.50363 | -51.54807 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a1ae276-60b1-356b-9444-588ad3135c69 | -12.09305 | -47.57952 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2055ca67-dffc-33ba-918c-d28b4ac6b789 | -14.21379 | -46.2452 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 316f8ae9-9771-3c6f-a286-0fa61355337d | -11.49726 | -43.6366 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc869f5-c735-3449-b1ff-62d416126287 | -12.09392 | -47.57444 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb79cc3c-ff81-3d80-8d3d-6813a08764d9 | -14.41835 | -46.40849 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 599c7ef0-ea6c-38af-a840-0a2af611808e | -8.93823 | -46.72781 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
