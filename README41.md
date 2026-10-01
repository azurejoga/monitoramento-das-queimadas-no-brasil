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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 365aba92-3d5e-31df-95f2-f0d1e05c4c7f | -18.06464 | -44.52308 | 2026-10-01 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9aeef9eb-1a42-395e-81e1-dec5f3aa7dc7 | -11.8255 | -49.51259 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c385613d-f40c-34d1-9f8d-43e5ee05b237 | -12.70617 | -54.06613 | 2026-10-01 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351d5028-c23b-3675-a58a-6af1fa374d77 | -19.23457 | -42.94732 | 2026-10-01 04:17:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f10fdc69-d2a4-3ea7-98f8-6e371fd77e3c | -13.54993 | -49.18032 | 2026-10-01 04:17:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eecffb1b-9b94-3199-9797-f217b9382d0c | -13.38007 | -46.81171 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1154fb6c-f36b-36ef-8e72-203be0bac988 | -16.42614 | -40.86646 | 2026-10-01 04:17:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fde5da14-9067-3458-bd9c-9aed16f21598 | -17.09183 | -46.81696 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b58861a6-6559-3e92-b94b-279975bee011 | -17.00107 | -45.46838 | 2026-10-01 04:17:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 405a3be0-189e-3385-9e83-8bcdd17507e2 | -17.91233 | -44.26438 | 2026-10-01 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 909c3d00-8602-36c3-acb1-2694cd3628dc | -13.37969 | -46.83766 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56a42294-398c-3121-8595-79932fe1cc1e | -16.14778 | -42.86534 | 2026-10-01 04:17:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd6187c2-f0e8-353b-bea5-8fa72d1cf7b0 | -17.30871 | -41.8389 | 2026-10-01 04:17:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7100d459-04b3-3f0b-9edc-d10bb36e3a7d | -11.26227 | -54.81499 | 2026-10-01 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5fbc9b8-f671-3a5d-b24e-3801b016503e | -17.64853 | -39.66563 | 2026-10-01 04:17:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5b6bfca2-59da-3409-b2f8-ba71207b6f27 | -11.79947 | -50.51344 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02abc9fa-8f9e-3f7e-ad88-3d8b0d2cb9ae | -13.38038 | -46.83375 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bde3e8c7-f1af-3fd6-a960-23ade1fb90dc | -14.49862 | -48.31064 | 2026-10-01 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95e1ff64-b38e-3aa2-ba7f-fc26201e55da | -16.52494 | -46.86143 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eb8630d-0d22-3724-897c-1496b82deb14 | -15.95529 | -41.89661 | 2026-10-01 04:17:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 48e26f14-4ea4-3854-94e3-9c336c913e7f | -14.43575 | -51.26034 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9c88604-7219-3bed-a895-38f1d7e51e65 | -12.86671 | -44.33587 | 2026-10-01 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 146f10f7-15ab-3657-85b1-4a5ac0cb999b | -12.70942 | -46.95698 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87eac40b-b758-3b33-b1b9-2dc4d30a46bb | -13.65855 | -53.94613 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d063a564-d6fe-3b5a-b058-07934a3d39ff | -14.88902 | -51.88695 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57555677-76d8-3fd3-ae62-c6106e68b412 | -13.10167 | -47.44357 | 2026-10-01 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a18b1dd-2b4d-3b5c-942b-c0a1932a40a5 | -15.22574 | -46.15038 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b295611-da3d-3474-bd0b-74b7c8918149 | -17.52531 | -43.73384 | 2026-10-01 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da623ae7-703b-31dc-8813-be76419c37f7 | -12.03055 | -51.02061 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5abc93c2-712b-345a-adda-4f07ea3a1f0d | -12.09399 | -50.69202 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7594d021-42fd-3e02-8beb-92c7d519bb0d | -13.38352 | -46.82972 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 204520c9-7936-3e93-92de-3ec7998ef536 | -14.37107 | -44.78043 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eb1c4046-48ae-3a83-a72b-04086f29bfcb | -11.82091 | -50.52794 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f94cdb48-ae01-35d4-9d1f-fe7bd76b9d63 | -23.50595 | -46.61096 | 2026-10-01 04:17:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43dc267d-ae4e-3a2b-87a4-aa5285ab1754 | -12.77423 | -47.26709 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf886e5-d763-3b1c-8c10-383e497ce6c2 | -13.1824 | -48.50915 | 2026-10-01 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87b446ac-7023-3fe3-970f-d248f188723e | -14.43367 | -51.27071 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a1d5109-c0fe-3315-bb23-f819982fec8d | -11.82159 | -50.52451 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b7204b4-5f57-3586-8bf1-1771b87e1d65 | -16.5446 | -41.79844 | 2026-10-01 04:17:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3e4c0f75-1d42-39a0-aea2-787de6a4daeb | -13.3882 | -46.82724 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef4ab580-d57f-3d69-9529-3db3c5618717 | -14.14271 | -51.13165 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05dfb273-1e33-381e-83f1-a04b6022efb6 | -14.39056 | -51.29044 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b473641-71d8-3814-ac85-1a10d0361803 | -15.23718 | -48.56568 | 2026-10-01 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8684d1d4-2cef-38a2-8008-5cce12b8c80f | -13.42619 | -43.80881 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 719d86bb-9bcb-39c2-ac8c-4a474f63ad24 | -13.32412 | -43.47322 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97ee3593-2b2f-308a-8592-a7317faf1365 | -15.12824 | -43.62239 | 2026-10-01 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| feb88281-da7f-34be-8a40-2cc2f962a5a9 | -14.23647 | -44.23073 | 2026-10-01 04:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5d8089a-b229-3f19-a372-e9192e609cce | -14.15666 | -51.14539 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4038525d-ac7c-3854-b2ec-a188e797e6ce | -16.42973 | -47.1882 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4822e6fb-32ac-3501-8482-5155390a5255 | -12.37927 | -51.14648 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ff001c0-f19e-3c0d-9d7e-3d6bdcac3c85 | -13.38821 | -46.8134 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30f81466-f63d-3728-b57e-a55231214333 | -12.18316 | -47.38283 | 2026-10-01 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3b2d630-02da-3051-90ca-68fa8174142b | -11.79412 | -50.51235 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25c0f625-0c30-30c0-a4ef-026d27b11952 | -11.82761 | -50.52218 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6cae0a9-b642-37d6-b8d0-7008217f60f6 | -13.38573 | -46.82739 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e18a837d-937f-39ad-855f-17ba5a6afc76 | -18.10426 | -44.41353 | 2026-10-01 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b713f84-28a8-36a6-a47f-6cf3c49766b0 | -17.21953 | -46.844 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 426cc0ea-ff36-3b7e-aa51-4f71ebcb9282 | -13.38685 | -46.8346 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 150e8edf-bd80-3c8f-b0cf-906480cf67f0 | -11.7426 | -50.40662 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfe874ae-5d15-3a28-8f36-ff68adb5d0a0 | -17.87401 | -42.9034 | 2026-10-01 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59893870-3dff-306a-8206-49f12e2ce6c2 | -15.28865 | -42.77775 | 2026-10-01 04:17:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef771aca-5f81-3aba-8270-dcb9f6d0c3fe | -19.23066 | -42.95039 | 2026-10-01 04:17:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bfcc4f21-5785-3b85-bdd4-4e20b88077bf | -15.2365 | -46.14484 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77595980-eadd-3b5b-b54b-a575565b0ad1 | -16.02266 | -45.13465 | 2026-10-01 04:17:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 261bc418-82d8-3175-9252-93a4d2ae6a43 | -16.16173 | -42.86406 | 2026-10-01 04:17:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8c759c5-aabb-3804-878f-124749409ae2 | -13.37157 | -46.83575 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45457065-82ef-3a7c-b5b1-6e4e9540cb3e | -16.67878 | -41.85011 | 2026-10-01 04:17:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a8d3c977-4ccb-3b11-b134-2f06f237efef | -14.42576 | -51.25458 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a23a457-4587-30ec-b5a2-668c3cc59675 | -15.97423 | -52.48374 | 2026-10-01 04:17:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| caa234d0-d2fc-3536-b12a-ed9e7b188883 | -14.38378 | -51.29625 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2b3b1fb2-7b31-3e55-be50-2d163d3001f2 | -13.51097 | -46.88863 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 859962d5-7b9a-31e4-a443-e813d9154b55 | -16.43068 | -47.18295 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4ee3bc1-2711-3728-a0b7-b072310374eb | -14.35097 | -44.74644 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d2e9b75-9955-39ff-bc54-63a43c772cf8 | -13.5198 | -46.88668 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb00a4e9-bfd3-31b0-b1cf-e01819b9ec18 | -15.24002 | -48.56371 | 2026-10-01 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 578da31b-cbc8-3ca3-9fca-ad7baeea27a8 | -13.33194 | -43.96005 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 751eb5e2-5abd-39b3-95b6-e652565e90ae | -11.1721 | -54.11391 | 2026-10-01 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f1d4edb-bc58-3c02-9ef8-5d63499efa21 | -14.40551 | -51.2719 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6adf6b72-9391-3e11-af9e-9a20aa055091 | -17.47636 | -43.56176 | 2026-10-01 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dbad6a4-f00e-3e21-afdf-0d9c176a2eaa | -17.90956 | -44.25995 | 2026-10-01 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5ac7354-06f6-3ab6-8274-25bdc1155f85 | -13.42553 | -43.81273 | 2026-10-01 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff0ccbeb-65bb-3f7e-add5-28c92c3baa2b | -17.08322 | -46.82044 | 2026-10-01 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9625c95a-2780-376a-bcd2-33f2e7f6a4ab | -12.64627 | -47.64005 | 2026-10-01 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b71fd6b9-6a8f-388c-800e-514ac6b80b1b | -14.14665 | -46.23974 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b88a7e2-f21d-3081-8408-1fd0b7184ff8 | -14.4311 | -51.25573 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96c8a0e9-7e9b-38a9-a242-6206774d23d4 | -14.3948 | -51.26962 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7ed64d46-1ca3-3b89-97b2-903792de6b45 | -15.63152 | -44.73794 | 2026-10-01 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d10f7ff7-52f0-32c4-9690-28610523cf22 | -15.97228 | -52.48308 | 2026-10-01 04:17:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 273e3937-5661-30e4-a6f8-a8139f94fe3c | -12.18917 | -48.43948 | 2026-10-01 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| aed517ed-e622-3a1a-a525-17d337392b8d | -15.77361 | -46.02746 | 2026-10-01 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57b1bc81-d722-3508-9513-d56ae723414b | -15.22867 | -46.15617 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 174c6a3e-2910-3e0d-93f8-1aa70b88efed | -16.11666 | -42.22289 | 2026-10-01 04:17:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ca47262-2c90-32a8-a58a-817a25f184cb | -12.85884 | -44.3387 | 2026-10-01 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 77fa1890-caaa-39c3-a320-560e86e03c30 | -13.88715 | -44.45914 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b39ed08d-c19d-3874-baab-034ebb836988 | -15.25093 | -44.83451 | 2026-10-01 04:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29d99b6c-82c6-323b-a64d-0f7d8ad3e4d6 | -18.22641 | -42.75114 | 2026-10-01 04:17:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 90a1cce5-7f4c-3321-b248-f8beeda7a74f | -14.40086 | -51.2673 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 10a0e09b-f63c-39f3-a4d2-d0c5fce60480 | -14.44179 | -51.25804 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04b92993-1f62-3d3c-a03b-4ddc58bcbceb | -15.25731 | -44.81857 | 2026-10-01 04:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2587781-5e46-3f5c-b457-f19c74f3f723 | -18.1036 | -44.41746 | 2026-10-01 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README42.md)
