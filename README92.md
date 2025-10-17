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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e311e836-27f0-3f19-9ebf-60ea39db2fde | -10.50581 | -43.44122 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 68c347bb-fd76-3d8a-8e03-9d7da1635d44 | -13.82787 | -42.34855 | 2025-10-17 04:51:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e4fc2e1-ab43-3ec1-b18d-da8b9a7fa059 | -10.17268 | -44.78815 | 2025-10-17 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ffac3e6f-2605-3ebe-979b-f00dafbd927d | -11.47047 | -44.25587 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fbc532d-0392-34d0-acb0-671be2f44b6b | -10.28236 | -44.05235 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 038e48c2-715e-335f-a48c-1fc716cdcef5 | -10.11146 | -44.62654 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bef2c73-2e9c-3c58-abaa-87d523f5ea3b | -14.92029 | -46.7259 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 181125d9-30d5-340e-9562-17412d5a4115 | -10.65078 | -45.24904 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0ddde53-501f-39a5-93c6-028db99459ea | -8.26118 | -44.07869 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e82116ba-110b-3fb1-8d61-a7e6af5aaa8c | -8.45648 | -44.17845 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f8481e9e-af35-3eb8-8108-6e1456959582 | -14.32844 | -51.4776 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2c719c6-65df-33fe-afac-f6ac8add4097 | -9.6207 | -49.12843 | 2025-10-17 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbf56852-b1b2-3710-a617-22aa59ed911d | -13.38977 | -47.21305 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68dce5ed-d3e4-3efc-954e-1a06c3adaeb9 | -10.64811 | -45.30114 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d87cd57-4a54-368f-87d0-fc22f1374288 | -14.34481 | -51.4384 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47ba2554-54e4-3240-b8bb-b36c888f2e57 | -12.31583 | -45.63802 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 289f4cbd-48f9-3477-90a1-9927bb6a5700 | -10.25907 | -44.03947 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 077fcd04-b4d2-3748-92b6-e0bd5c4495e9 | -13.93769 | -48.68817 | 2025-10-17 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06453dad-b44b-3387-9bd1-d8f28713cd84 | -8.57271 | -45.43914 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5af543a3-0bd2-32e6-8226-53582b61fb01 | -11.4728 | -44.19912 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0875d047-22a0-3fb8-947c-1684e1b740bc | -11.37694 | -44.19108 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d3adc1c-3ad1-3fd3-a78a-e2dc97150710 | -8.63099 | -54.62791 | 2025-10-17 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 476bbff2-d449-37d2-b9ca-a5357777f534 | -11.5421 | -49.92204 | 2025-10-17 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e7b1ce8-89db-33b0-b8b1-88b983a3a2b7 | -11.48162 | -44.28573 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06778f01-fe93-34fe-9a78-38d1738ede1b | -8.39862 | -46.22992 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbb67fdd-2c82-33fd-a090-230b81388a9e | -9.09015 | -46.6838 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b940fd52-4974-385c-8b79-b9deb457a024 | -14.33578 | -51.47497 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 195abea6-573b-3fb5-a413-dc59e15c6f25 | -10.50737 | -43.42919 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b088e5cc-2f7a-3598-92f8-6a2de65715b4 | -10.93533 | -50.77694 | 2025-10-17 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46481502-61a1-3978-8613-81d93a5f895d | -10.53245 | -49.55093 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| b90f17e6-d045-321e-b108-b0b5c5e488bb | -13.39743 | -47.2191 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 337d61e4-9e4d-318f-9e7b-5c51112ed1aa | -10.26966 | -44.03529 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24473bc5-acee-3445-809b-b91bdf9838ea | -13.44286 | -47.94619 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5f765a2-4268-3290-b81e-a4ab1b30f7d1 | -8.45173 | -44.1778 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a1f14159-ade4-3c1b-ab58-c4e7d0ced89f | -10.50885 | -43.41784 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b3294dd-4d6d-3e2d-863c-f1fa918706fb | -10.49851 | -43.4167 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b7c10e1-d193-3493-a26a-1ba35f324e02 | -12.41242 | -51.30742 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4d07b909-360b-3cf0-8efb-8d46034f71c0 | -9.44638 | -56.65463 | 2025-10-17 04:51:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b439c29-65a8-32b0-b998-6d0ca9971979 | -13.27224 | -43.13539 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3762c3af-aa2d-3829-8fc1-f30267ed018d | -11.45774 | -44.0397 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 220f764b-b721-3ed9-a547-c83f1aeba416 | -9.03313 | -47.71922 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 597722de-6d16-370e-aed3-df4ca91dcc15 | -9.16241 | -41.05586 | 2025-10-17 04:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 22be8f5d-7fd1-300f-b5e2-f585c9caef13 | -10.28444 | -44.03718 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7623e12a-c462-3e92-9ef8-8d42bcf7dd56 | -10.97867 | -47.91022 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3338897-54f5-38ae-846b-26da24e46690 | -14.32897 | -51.42826 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f327b9eb-2ae2-3799-9a91-165dd917aae1 | -9.31021 | -46.93433 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7adf97f-9789-343a-94a3-6887152a1730 | -8.27537 | -47.11343 | 2025-10-17 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23f18d77-6b02-3001-a004-556bf7694dac | -11.36423 | -45.27462 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8472758-75a4-3dd7-8e4b-5a8ca00d4f64 | -8.7309 | -43.87635 | 2025-10-17 04:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a89297d7-12fc-39a8-be02-19282b04d161 | -8.93963 | -45.24287 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ceabee2-78da-375d-bbb9-1ede4ea79981 | -8.06705 | -45.41511 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5fcf5af-582a-3b9f-8814-705c65c95ea8 | -10.08447 | -45.33851 | 2025-10-17 04:51:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b25d3377-8cf1-354f-b08f-d34076e084db | -8.43686 | -48.70298 | 2025-10-17 04:51:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5750083d-49ff-389a-be0c-383e1e9e9461 | -11.97242 | -46.55566 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a53bef57-deac-304a-b412-2f9f7fd586f6 | -10.61772 | -42.30896 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc09e35e-3c49-3834-a6bb-6ccf1de7af9b | -9.5758 | -49.11329 | 2025-10-17 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2973de63-8731-39eb-96ae-144c5ce6d563 | -9.88558 | -49.11733 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b982911-8d3d-3903-a0f9-243b93a7a3d3 | -9.25844 | -44.35194 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f02b529-c9db-3db6-87ae-1ad5a94dfe2f | -9.34595 | -46.91315 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4725b613-0218-38ab-9936-01cee1870998 | -8.83969 | -44.40081 | 2025-10-17 04:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a4c8c56-a442-3fed-9505-66afe0683903 | -12.77074 | -44.88448 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c960ca3-5833-35fa-bb35-0ecd247e72cb | -10.51701 | -43.39544 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2947df6-e1b8-3b81-890b-02e69e93f4cf | -12.42701 | -51.3023 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a98a366e-7049-3082-a61b-0919a07a6bf3 | -8.51012 | -44.56686 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5bb8c8e-ccc7-3a1b-bcc5-a7a6bcaa4540 | -8.08197 | -45.43478 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 92a73d8d-7e17-3d0e-a5ea-6304fcb9ffd8 | -8.83786 | -45.98033 | 2025-10-17 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80e49b0b-f683-347e-acd1-0c073719a73b | -10.01066 | -45.64016 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 633f3b7d-8d9d-390d-a984-9453ffb018c7 | -8.08916 | -45.41517 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ca5c410-da2b-3cd4-9c7b-8c9c7bde218b | -10.81634 | -43.93664 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 171bbbd1-20b2-3e72-b8a7-4210006aefd0 | -13.04559 | -47.3173 | 2025-10-17 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23128602-29bc-3ed7-9811-61f07097ddac | -12.30728 | -47.2564 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c429fd70-a968-379e-8be2-9a581ea8b9bc | -14.3403 | -51.4681 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e1d7290-d25a-397f-8e77-f684d462412b | -8.93102 | -45.24806 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d7a9e99-171b-3b4d-b97b-48f4612ed88c | -11.47921 | -44.18854 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27988b2f-af2a-31ac-9d3b-3c8f00b63bbd | -10.85019 | -51.28696 | 2025-10-17 04:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85dd83c2-f3f3-3d36-93ed-baeefc5282e1 | -10.61635 | -42.31338 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2eca258-4278-32ec-a2de-d77b87ff9886 | -9.2537 | -44.35123 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3e720e3-29ed-3f00-80d4-6936b3015b9d | -8.3322 | -46.23457 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8eb71e74-4537-3c6c-a0e2-b69b14463a72 | -14.72266 | -48.30598 | 2025-10-17 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18fa340d-0ee4-35c4-9a87-6d9b7b1b4784 | -13.4158 | -48.58405 | 2025-10-17 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b4b0176-95a3-332b-83bb-43d83ac5ac12 | -10.92248 | -47.86346 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 054315a2-1d68-32cc-81da-637ef40abe5a | -8.45958 | -46.24497 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8630612c-d8aa-3386-b854-06dc7e05f061 | -9.9767 | -47.0155 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a55fad77-042f-39d6-83f7-5e7c5abfea38 | -8.39809 | -46.23363 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a76182d8-ba5b-3b6e-8ae9-9c92b77070e9 | -10.51662 | -43.39844 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1036155a-88aa-3cd9-9d61-503e8d1741d4 | -10.65094 | -45.25214 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 336a6d62-b5a2-3d92-8830-7e3e18aea9ad | -9.13626 | -46.65052 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3625d74c-1a3d-369e-8a3a-5ac51d4c076a | -9.6201 | -49.13243 | 2025-10-17 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9226a233-a6d0-3478-afb4-c7a8041f7b42 | -8.40382 | -46.22301 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2efd0219-2cb0-3cc9-8eb7-22fda095e2de | -13.50735 | -47.1646 | 2025-10-17 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ea65022-79d7-3aa8-8344-776924608da5 | -8.56835 | -45.43854 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e9e9494-6f54-38f8-888d-036e95e4c739 | -14.34708 | -51.44637 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ceea80fc-8f45-3912-8468-e45635761023 | -13.41715 | -48.57471 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dc6c4f3-60b7-3331-acbf-282ee70f7d67 | -10.92584 | -45.41687 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 243ca05c-c88f-3c2c-bfd3-7fdea3119c7a | -10.28937 | -44.0378 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 960c9203-e02e-30e4-a7f8-0dc3469d037c | -9.17011 | -46.73452 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49a61195-8ef0-36ea-8037-6eca21218770 | -8.52329 | -44.57397 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9648feaa-21b3-3ca5-8948-4409ed256a6c | -9.34343 | -46.91442 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6eac7d7c-2af7-3492-9cd7-f0bb48afc417 | -9.13544 | -46.59905 | 2025-10-17 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc76d670-268a-3d86-96c9-4bcb586c758b | -13.93389 | -48.68745 | 2025-10-17 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README93.md)
