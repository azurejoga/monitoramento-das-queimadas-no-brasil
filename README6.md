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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa283382-35b8-39aa-b714-ec320debbfcf | 2.65068 | -61.30455 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cbfb7d92-e7ec-33e2-a17d-e4bbdf862812 | 2.64918 | -61.2954 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 113fec85-a179-33f2-bdeb-197d05ec80ef | 2.33503 | -60.38795 | 2026-03-22 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d185ac6-59d3-34ad-a746-cc51364d337b | 2.64617 | -61.30531 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b62ab2b-7ae8-3efe-9ee6-cd5c69bd4724 | 2.65369 | -61.29457 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 60657327-02e5-3a05-94fe-c61e824741cc | 2.65444 | -61.29914 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 26589628-f210-39bf-b552-72d2d2cfb7e3 | 0.98533 | -59.38784 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 470f3a7c-1ecd-3750-b36a-e998a7b58f99 | 1.15999 | -60.33093 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6f4f496-186f-3967-ba99-fc7f8a9197e7 | 1.34619 | -60.02914 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b1e9e08-60fd-3fc0-a238-8d1122272070 | 1.16018 | -60.32995 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b128a4ee-6899-3104-a58d-83d96583d846 | 1.95762 | -60.62617 | 2026-03-22 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e22bb4e-ff4c-300c-b39f-7554e49fa7d1 | 1.08314 | -59.73259 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 462ce104-f40b-32c0-ba1b-8dca4a2016aa | 0.99408 | -59.38657 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b989562-0323-3252-a87d-846902291084 | 1.34571 | -60.02621 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 613d44e3-26cf-3f39-a02f-580b87e7362b | 2.12266 | -61.22356 | 2026-03-22 06:05:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33fb1a42-3871-3701-9d8a-e1211b8d29a4 | 0.99063 | -59.38702 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4a7a8ab0-9569-3fdc-b630-29c26759a9fa | 0.98378 | -59.37803 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 531c4a97-29d4-3d73-9548-c9e33ea586a4 | 0.57548 | -59.90791 | 2026-03-22 06:05:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2452af7f-f2a2-3658-bf73-35cfee039e6a | 0.9824 | -59.3817 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| caf546a7-6f62-3d2a-adab-c8c48cc55fb4 | 0.9843 | -59.38132 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fa8a419c-5e8e-3ff7-a2dc-c50bee8d8d61 | 0.61647 | -59.86689 | 2026-03-22 06:05:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e8a72da-f5c5-3b74-a6d0-8516b7b72f40 | 1.04724 | -60.36301 | 2026-03-22 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bccb7c2-eb91-37fe-8aef-4ff5c9a8fe5f | 0.98878 | -59.38738 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4b8d6e5b-b552-3fbf-bb9a-99cc167047ff | 1.21487 | -59.97575 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28886352-d49f-39f1-84eb-b809f0870494 | 0.98715 | -59.37755 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4154853f-3ae4-3685-91a1-93f6eb12256a | 0.98481 | -59.38458 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 114c6a08-4f39-3c26-9b17-53a94f05e050 | 0.98325 | -59.37469 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e296027-6320-3487-b3e1-33ed35f450c9 | 0.861 | -60.24958 | 2026-03-22 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be7109ca-3bba-3701-b89f-470d5338f524 | 1.2093 | -59.97358 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed2f7009-c04b-3908-ba42-ee965c4d7580 | 1.25546 | -60.45026 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41a791f4-c4f5-38a4-afb6-7252aa262649 | 0.66348 | -60.60784 | 2026-03-22 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08b464fe-5fba-374f-ad18-cdbb8f1c9b94 | 1.122 | -60.18649 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa637033-6879-37ef-84ad-c4e7e5e85470 | 0.99245 | -59.37669 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f3bea6a-d044-3bc2-9504-57972e134678 | 0.9877 | -59.38084 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c01932ef-a804-30e0-9d3f-b10c2f4ad584 | 1.41627 | -60.75868 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c43a865-1117-3455-acc7-e8098e09dace | 1.2546 | -60.44479 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2616e8f7-c05c-3869-850b-b8c36c962d7c | 1.08664 | -60.34876 | 2026-03-22 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96db325a-8bd2-3ddd-9eb0-6d9e8ddabd58 | 1.5513 | -60.25142 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6c15863-7301-3580-8247-c534561f5587 | 1.12107 | -60.18579 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 561f3524-e0c4-3368-83ea-1a9edca9f991 | 0.99299 | -59.37999 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e85b0898-8001-376b-a719-1502bf1d617e | 1.04637 | -60.35747 | 2026-03-22 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2c142c2-f60b-3d22-8519-e16725100f82 | 1.1211 | -60.18077 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91be58d7-e252-3bdd-80e6-d15c3dffa748 | 0.57083 | -59.91182 | 2026-03-22 06:05:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e7a631d-544c-32b6-b1fc-44ee68538d50 | 0.98907 | -59.37714 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a173e819-f176-371a-86e0-9f6fc5fa6ebc | 1.97785 | -60.56976 | 2026-03-22 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de6ed954-ebc3-30a7-a4ec-e9f0d82067a6 | 0.99354 | -59.38328 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99cfac94-c8d1-3db2-b041-9313c10f2362 | 1.55164 | -60.25046 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14849100-b558-3742-849c-3930c9906fca | 0.98294 | -59.38495 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0ca4ecf8-ddbd-3d85-ab64-ae77c9e304fa | 2.05538 | -61.81441 | 2026-03-22 06:05:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66910ff5-ea23-356f-b340-c639de028139 | 1.21435 | -59.97263 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d059d9a1-397e-379e-aabd-a38433e2e15a | 1.64554 | -60.29779 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83d269c6-9f97-333f-883d-26512739989f | 1.95717 | -60.62233 | 2026-03-22 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0580a85-d5ba-3ab9-8b8c-53297d07d117 | 0.98824 | -59.38411 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 02c5673d-1a64-3061-88e9-f34bc8b04d01 | 0.98959 | -59.38044 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d72716a2-5408-3e0b-9983-2a5199f563b2 | 1.41733 | -60.7598 | 2026-03-22 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 382601c5-74e5-3e8e-8068-4152f451194e | 0.98185 | -59.37843 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 16ea6c5b-701e-350f-94b8-cc006e3a83b1 | 1.08264 | -59.72955 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c5ad991-bb8e-35e2-976a-0c99252f14da | 0.98348 | -59.3882 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d1038307-6390-351f-9705-b0eddd723f80 | 0.99011 | -59.38374 | 2026-03-22 06:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0a3b65f8-6167-308a-b130-2f68e284860b | 2.05467 | -61.81012 | 2026-03-22 06:05:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42e9b7cd-df08-30fe-9960-ec028d8f238b | 0.85047 | -59.98944 | 2026-03-22 06:05:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65928b6a-e3cf-32a1-a095-271346d24a57 | -9.04737 | -63.33235 | 2026-03-22 06:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18851334-ec8f-3b2c-957a-c50d8c0d7daa | -9.04806 | -63.32731 | 2026-03-22 06:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75ade853-8530-3b9d-8050-d4af39262cae | 2.64228 | -61.30722 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 161d84f7-43a7-35e7-b722-84f78ca457e2 | 2.65396 | -61.29692 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8bdb0f42-f8d2-3b04-bd3e-86decb185a44 | 2.64575 | -61.28675 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3b523a2c-0fc0-351e-9d2f-a26c348028e6 | 2.64824 | -61.30486 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 95047ee8-457c-354a-a299-7e5da57cfcb0 | 2.64801 | -61.29962 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 300d39a6-4530-3e03-974a-969d22043384 | 2.65288 | -61.2905 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 50f2ff5f-c0ad-3b1f-9878-50cb5d4ed596 | 2.64113 | -61.30072 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ce984b94-7865-3253-ba39-f8005c93ab6f | 2.65369 | -61.29172 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f749e8b8-935e-3f81-8ad0-add8cc4a7f9a | 2.64137 | -61.306 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 800042c1-1ed6-39bf-bd2f-72a9ac27636d | 2.64496 | -61.28547 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a97a6236-cbb9-349d-bbf7-ac7e5183bcf5 | 2.65506 | -61.30349 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a49d8ef6-30e5-3e51-9a6d-d47190300c18 | 2.65259 | -61.28543 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 54dce3bb-e703-3e6e-8d86-bfb7f07b5b30 | 2.64687 | -61.29318 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 42c45e92-0486-3a7b-80f7-5ebf431e13cb | 2.64715 | -61.29841 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| dd087f8f-aef0-3c8a-a9f9-461bf2a4f4f7 | 2.65597 | -61.30474 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 66ca450d-276c-3dba-aaed-adb8f6f807ef | 2.65482 | -61.29818 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c58c2727-9564-385b-b8de-aec0f31078c3 | 2.64914 | -61.30606 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f0208d71-118e-3f8d-b016-dc03ab408d79 | 2.64606 | -61.29197 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 52feafcc-302b-33f5-ae38-13fbe0dc1184 | 2.65182 | -61.28421 | 2026-03-22 06:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6d0a47cf-d2d6-39aa-961c-0c56571b76a4 | 0.98161 | -59.36993 | 2026-03-22 07:12:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 62745069-3d48-378c-bdea-2e42598bdc7e | 0.99305 | -59.38618 | 2026-03-22 07:12:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 327729b5-a5c4-3314-964c-5d2c2a456708 | 0.99172 | -59.37741 | 2026-03-22 07:12:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 14910aee-36ef-3aaf-8744-47b650f2e9f0 | 0.98426 | -59.38747 | 2026-03-22 07:12:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| beb0830b-725a-3a38-babf-f72853fb86cf | 0.98293 | -59.37869 | 2026-03-22 07:12:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 1d4714b7-cc12-3d30-868b-1facf5bd9b17 | 2.64859 | -61.28642 | 2026-03-22 07:12:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 69e8bfdf-a0e6-3cd9-a4de-195ae9565a5e | 2.65022 | -61.29724 | 2026-03-22 07:12:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7bd3100c-2c91-31aa-9df9-48010b3b0b62 | 2.64051 | -61.29865 | 2026-03-22 07:12:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 55cfbe24-a71c-3021-a675-2eef0d2cbc0d | 0.99039 | -59.36864 | 2026-03-22 07:12:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3fe2b0b0-3bc9-3471-befd-565882a80bd2 | 2.65831 | -61.28509 | 2026-03-22 07:12:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3e63ddc7-de08-34b3-b995-9a6340633992 | -10.539 | -39.39344 | 2026-03-22 11:30:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 00d14f40-bd00-33b4-9832-2c788afd61fa | -11.84131 | -37.93591 | 2026-03-22 11:30:00 | TERRA_M-M | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 40f66c10-7476-345e-bfe3-b26276294827 | -9.21357 | -36.94623 | 2026-03-22 11:30:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 987c38f2-48a3-3383-88cb-516b8cacbd52 | -9.21492 | -36.93639 | 2026-03-22 11:30:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| b667c970-96e9-382b-95ea-e5688a536044 | -11.84 | -37.94547 | 2026-03-22 11:30:00 | TERRA_M-M | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| a9f86a0e-d3fe-3826-9177-eff19119e100 | 3.913 | -60.9395 | 2026-03-22 13:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 4b70e1f0-4007-3865-90da-bcfd717e611f | 3.913 | -60.9395 | 2026-03-22 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bc7a961e-b3cf-3271-82d2-87151d19eb85 | 3.913 | -60.9395 | 2026-03-22 14:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |


[Clique aqui para ver as próximas entradas](README7.md)
