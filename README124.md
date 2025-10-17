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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5529c644-e856-3052-9310-7d7e07666344 | -9.9638 | -47.0256 | 2025-10-17 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| fd083859-1dd0-3ac0-bc71-ccb4f3900146 | -11.5724 | -44.0736 | 2025-10-17 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f6c1c78c-cdbe-3555-867d-462f9225882e | -10.8101 | -43.9275 | 2025-10-17 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ead468d1-c669-3eb8-9e83-4aebf3b15b67 | -11.4547 | -44.2316 | 2025-10-17 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| a924c267-a78e-351e-a14a-2371523a53eb | -10.5132 | -43.4289 | 2025-10-17 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| fdec9ca4-bb5c-3728-a50c-ee56a58d36dc | -10.673 | -45.3125 | 2025-10-17 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ba65757f-3de0-3556-97e3-dc6192281f96 | -12.699 | -48.6299 | 2025-10-17 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6aa474e1-c80f-3221-87cf-6eb0056aff18 | -10.938 | -45.4146 | 2025-10-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| c3ac1637-3cd9-303d-abdb-b185a8c7acb6 | -11.3972 | -44.2401 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 737ae223-9475-3211-b0de-29b55af810c8 | -10.9185 | -45.4401 | 2025-10-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 67adc7a6-301e-387c-9e9d-a6828ee255cd | -10.8293 | -43.9248 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 63f545a0-72a7-3192-8b74-9f8cc353f0c4 | -13.0488 | -47.3131 | 2025-10-17 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 51b75226-823e-345c-9bfc-306f642e55f9 | -11.0626 | -51.009 | 2025-10-17 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 7c74e180-65bc-3f05-801a-c7aef7b053cc | -11.3992 | -44.1229 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5591a4a1-9446-39c9-a95e-86502349fd92 | -10.1063 | -47.6525 | 2025-10-17 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 061793c2-8751-33d8-b1df-0937da6acb28 | -10.5132 | -43.4289 | 2025-10-17 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 0fe66631-1ff4-3020-873a-bd5b9fc346ba | -10.5834 | -47.42 | 2025-10-17 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 4ebfde95-7285-3662-b512-55a12097cb59 | -11.5921 | -44.0472 | 2025-10-17 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 175.4 |
| d3c6ab19-8eb2-3e00-8791-fae3b717f7c5 | -4.4248 | -43.3805 | 2025-10-17 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 0ae10871-4e59-3b33-bac2-a077cb4f0e2c | -10.6169 | -45.2512 | 2025-10-17 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d4c562f5-24ed-35d3-a9f8-191ecbab2466 | -12.9459 | -41.8082 | 2025-10-17 13:50:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 332d9b02-5127-33a8-9431-98d9b2293c61 | -12.4678 | -45.4694 | 2025-10-17 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 0ca28aac-3710-33ac-9cb0-944e4cbdbf8e | -11.5912 | -44.0942 | 2025-10-17 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ed8e78fe-48b3-3d5f-a83d-9cd378e535ef | -10.6028 | -47.3955 | 2025-10-17 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| a390b4f7-ea99-327c-9ade-7877d131b302 | -10.673 | -45.3125 | 2025-10-17 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 00549720-418d-3a53-99d0-e824ac06d758 | -12.4866 | -45.4895 | 2025-10-17 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d6b58e9e-e471-3387-9deb-2d8191d72b79 | -4.0274 | -44.1877 | 2025-10-17 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 1796b575-3abf-3c96-814b-5fbb8ead799b | -12.9607 | -47.9294 | 2025-10-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 26cd5c7a-4765-3a8c-a884-c631511e2d19 | -12.9259 | -41.8363 | 2025-10-17 13:50:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 92.4 |
| c31882cd-8699-3375-99b4-1c162bfec956 | -11.7435 | -51.1472 | 2025-10-17 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d69f3173-e214-3dd7-88e4-bf0545b93f57 | -12.9265 | -41.8118 | 2025-10-17 13:50:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 53f8c4c9-6b31-3bbb-b1a7-0f867f683b23 | -12.2648 | -47.1571 | 2025-10-17 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d4a6678b-6390-3994-9951-b28202f00ecc | -10.5128 | -43.4525 | 2025-10-17 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ba3b3804-67e2-3d70-9b24-9921a934277e | -10.6726 | -45.3355 | 2025-10-17 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 6fd8bada-f92e-3f92-9ed5-befeeb6697e7 | -12.0879 | -47.4277 | 2025-10-17 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 43e59257-97fb-3bb1-8c85-1f3486da08f8 | -9.898 | -47.6758 | 2025-10-17 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| aa6fe555-a2c0-3c78-912b-9eadfb018a3f | -11.5724 | -44.0736 | 2025-10-17 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 9b78016f-ca1a-30c0-9f07-6bf146dc1cbc | -10.9938 | -47.9019 | 2025-10-17 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5bcf09c0-cf16-3d26-b0fc-a67198076e79 | -11.2642 | -45.3011 | 2025-10-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 97440d58-44bf-35a3-8dbf-35e018f0e8d9 | -10.4941 | -43.4315 | 2025-10-17 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| b40029c5-8074-3377-b7ec-e5650942f324 | -12.5059 | -45.4866 | 2025-10-17 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b9c407dd-f7a1-31d5-9038-219804532340 | -4.0088 | -44.1887 | 2025-10-17 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| fb19ba6b-8638-3b26-8e51-24490bfe4124 | -10.9376 | -45.4375 | 2025-10-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| a717764b-d8b6-36e3-ae53-5335f27bf6dc | -11.4164 | -44.2373 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 91f0f1b5-fb64-352c-b3ce-4c39113fb22a | -12.6871 | -50.5017 | 2025-10-17 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c0673901-582d-3019-b07b-c0fab7a2eeba | -5.4561 | -41.0054 | 2025-10-17 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 275.1 |
| bf81b882-4fe6-3e45-ad46-02ed734c93d0 | -13.1322 | -46.9629 | 2025-10-17 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d468a0af-5135-3dd8-9b44-12f9f5fc8353 | -11.4193 | -44.0731 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 24383bb4-f16d-36f9-8640-211290325a5c | -10.9189 | -45.4171 | 2025-10-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 38797972-5fec-3da9-b7b8-d2259d31a141 | -10.5837 | -47.3978 | 2025-10-17 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 02c73225-f619-3e91-9ff8-c159c470102b | -9.9638 | -47.0256 | 2025-10-17 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 401c2289-5099-395f-aa05-821da1cac75f | -3.9822 | -42.4924 | 2025-10-17 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| aad704e4-6dad-3240-955a-09bc57097f03 | -4.1525 | -42.1989 | 2025-10-17 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 127.0 |
| 38c4af5e-4b6a-3bd4-9fbd-bf81bd10cd64 | -12.4264 | -51.3027 | 2025-10-17 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 87f29ecc-5540-3869-98e6-0213bfa83d02 | -4.1523 | -42.2226 | 2025-10-17 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| e6a6a997-ceb8-3dcd-94ef-5c5bea3bcc58 | -14.866 | -52.4193 | 2025-10-17 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e2faa9f4-169b-3740-acb0-0acc95c52cde | -11.4184 | -44.1201 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 9686e4b9-0fa7-37a5-a63f-44c80b4c45ee | -10.8797 | -47.9157 | 2025-10-17 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 6cd1b780-55f1-335b-94d0-44826cde3836 | -11.0214 | -47.3443 | 2025-10-17 13:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| c88db427-1c17-3e0d-a0b1-0c7c12d2f952 | -13.9127 | -45.5808 | 2025-10-17 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 780ca8b1-ccd8-3f55-9ad8-9c251021b2f4 | -11.3996 | -44.0995 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| fb3e4d8a-c2c9-30df-ad2f-ad77d672c996 | -13.2005 | -46.4084 | 2025-10-17 13:50:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8b104bf5-249b-329a-94bf-6f55ff356132 | -14.1754 | -47.9252 | 2025-10-17 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a9059bb0-6c17-350d-b49e-0a0ea9e5fdd7 | -11.7622 | -51.1663 | 2025-10-17 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e03707f4-2dc0-361e-a029-b4aed9e959bb | -12.4455 | -51.3004 | 2025-10-17 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c8a2cd54-4d1e-336d-8fa5-4b1e2cbcaae9 | -5.2863 | -41.0673 | 2025-10-17 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| fed4cd0d-ccfe-376a-8d46-e7ec7aef2875 | -12.1678 | -45.0771 | 2025-10-17 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| fafbdfbd-8b4c-3f51-9210-9ad7e94643f9 | -9.9831 | -47.0011 | 2025-10-17 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 647d531c-6b70-3f5a-88f8-58cd39f2ef52 | -14.0905 | -43.6235 | 2025-10-17 13:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| a8097383-3421-311d-b5ce-99cdb0323433 | -14.8854 | -52.4167 | 2025-10-17 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| ece32a89-bb8c-36ee-9f66-e1a5d66163ba | -10.4945 | -43.4079 | 2025-10-17 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f6c1423d-6977-3cbc-8f4e-db78b95ea883 | -10.7562 | -47.288 | 2025-10-17 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e336370a-bc31-3fa6-b559-412811f7f38e | -15.0321 | -48.7478 | 2025-10-17 13:50:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 81cc9f01-8635-3f79-8fe8-d740f6c31ada | -9.6409 | -47.1285 | 2025-10-17 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 863be253-c098-3924-9476-4a6954176ba1 | -4.4446 | -43.2164 | 2025-10-17 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 42a8fcba-4e18-3ebd-a0d1-c85ebe0d67fb | -11.3603 | -45.2646 | 2025-10-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4674513b-1a40-3e91-9b83-822a6622cc54 | -10.8101 | -43.9275 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7f02c3fa-1433-3f6e-a4fc-98d97ff8d8c7 | -12.284 | -47.1544 | 2025-10-17 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 2c457102-0975-30da-b652-1a34c56ba0b1 | -11.3988 | -44.1464 | 2025-10-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 1d2a0053-1cc9-3411-bc48-2c434a1fad65 | -9.9828 | -47.0234 | 2025-10-17 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 547335ea-d245-3d5a-aaed-d5a94c6f2410 | -12.1682 | -45.0539 | 2025-10-17 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 0030b404-cf31-3a70-b42b-4e415ec24b55 | -11.0623 | -51.0302 | 2025-10-17 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b023f099-5019-342e-bb81-ba7efe4b90ca | -10.534 | -49.5471 | 2025-10-17 13:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 453a67ef-56b5-3c65-a867-93ca34ab769a | -3.9635 | -42.4934 | 2025-10-17 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 770b5198-1248-3ba4-a0be-19f3b901d3ef | -10.5136 | -43.4052 | 2025-10-17 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 43bd9340-8aee-36a6-ac18-36f574c3264e | -10.9748 | -47.9042 | 2025-10-17 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 23a27027-7111-336a-a04b-e68cd7583b17 | -12.487 | -45.4664 | 2025-10-17 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 7e3aa8c6-d8ff-3c52-b19f-c9909243cc34 | -10.5128 | -43.4525 | 2025-10-17 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 185.5 |
| baee5a19-5244-3c30-997f-bfea611e8e1a | -13.0299 | -47.2935 | 2025-10-17 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 26cf7660-45d0-3f11-a9eb-362f17fcecc1 | -10.9376 | -45.4375 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f1f616ae-de0f-38e2-8ef5-50aa0eb7efd9 | -15.0516 | -48.7446 | 2025-10-17 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5a897521-50a1-3e81-b32a-ee6a346b82ee | -14.7434 | -41.5719 | 2025-10-17 14:00:00 | GOES-19 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 123.5 |
| a5db898b-c08f-39da-8d49-493b8164e779 | -12.284 | -47.1544 | 2025-10-17 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 78190227-12c6-358b-94a3-0530a6721d93 | -9.9638 | -47.0256 | 2025-10-17 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| c3a7b9a7-ab7a-3ffb-a150-690295438558 | -9.879 | -47.6779 | 2025-10-17 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2a69b49d-7041-3bd4-b064-7e6aeb1958e6 | -4.0274 | -44.1877 | 2025-10-17 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e39ba141-9561-387c-8365-5e9c94bdc614 | -10.2741 | -44.0715 | 2025-10-17 14:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| e5e9bc44-cf57-3f96-aadc-7323643677e2 | -12.487 | -45.4664 | 2025-10-17 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| f41ed7d4-24fc-3420-95f0-d4e6c183c968 | -5.8569 | -42.3407 | 2025-10-17 14:00:00 | GOES-19 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 37e1c60f-ea3d-3ef4-9cb0-59ca7b76e1f0 | -13.264 | -47.1233 | 2025-10-17 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |


[Clique aqui para ver as próximas entradas](README125.md)
