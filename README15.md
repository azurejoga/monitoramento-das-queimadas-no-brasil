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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b98cf214-e1e3-366b-be7a-ac28ae7af20f | -7.29 | -43.69554 | 2025-09-01 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 004ae6f7-56a9-3919-aa62-8de7fdcb3822 | -4.90944 | -43.18515 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e152f37-cf41-319e-9410-499c262d3e57 | -6.29763 | -43.62138 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0ed4643-68b5-349b-9431-bcedd7bf6866 | -6.83823 | -43.32671 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 86dadf43-20d9-36af-a60a-e97b1699a2c7 | -6.74791 | -43.78617 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b4f846c4-3822-3f57-a128-8e5d82cecdf7 | -6.4644 | -43.95864 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2485dc91-c194-348d-abf7-6083bd8add6e | -6.20081 | -45.3795 | 2025-09-01 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aba9834e-120f-3566-b036-9aa2372b62a8 | -5.66039 | -43.63873 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d76e75eb-ec62-3e91-969c-166b2f0354d0 | -6.35476 | -43.92085 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3baa3a97-55d8-3e71-add4-7c3d1a1d01b1 | -6.57198 | -43.70227 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5338d69c-087a-37f7-abf0-32d47b14ed7d | -6.83336 | -43.3259 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 347e3464-964e-3d40-b6cd-37e7e23e6564 | -6.19881 | -45.37501 | 2025-09-01 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fac7011-e829-3e48-9686-a02ada2d3afc | -7.06612 | -44.3453 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f9608eb0-8630-3835-8a44-13634650253e | -6.46333 | -43.96469 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 02c76973-4790-3991-9c56-a57d2963b426 | -6.29938 | -43.63876 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bcdde86-cef7-388d-b654-dba5207e4222 | -5.91628 | -43.44263 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8125890b-9b53-3bff-8835-d4f02eec6d16 | -6.30346 | -43.61568 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d63e7c35-2837-3ed6-bf34-89f5a33b2992 | -4.84098 | -43.01186 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b192df7e-7a9c-3d8e-889e-277be1ea5e1b | -6.35228 | -43.92137 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00a88ed9-a689-3579-9005-0f9aab674fa8 | -6.16104 | -43.33928 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fad604e-634c-39fe-a3ac-38429ed085da | -7.0799 | -44.35824 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a9cd4491-6a0a-3051-9cd0-32d1248a9d18 | -6.16397 | -43.32245 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d1cf8d3-8743-38c8-a968-348f698a2cdb | -6.30241 | -43.6216 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00586337-528c-3955-9892-0b039f02d4e8 | -5.95471 | -44.27338 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d2c9969-fc2a-3b68-b847-8b46ca4ded8d | -5.64376 | -43.65458 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a103dd10-5539-334a-8862-8c32a659dec9 | -6.51465 | -43.55611 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2de8c6f2-fed0-3df4-982e-2e525019429a | -6.31018 | -43.78415 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c15d66e0-59d4-3fea-bc6a-20419bae204a | -6.35982 | -43.55852 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c68fd07c-cb5a-3dfb-8d20-123d42f70b85 | -6.16301 | -43.32797 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f39e20f-7e0e-33db-91bb-fc56a37e2e55 | -7.08164 | -44.34842 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 85654793-0f69-3cd1-9e7d-826dbdf42f5e | -6.23499 | -41.81163 | 2025-09-01 03:42:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65026586-dced-3340-917c-f5773c9c0073 | -3.42574 | -43.33032 | 2025-09-01 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74cadebe-5298-34b4-bdf6-d3d7affcf277 | -4.92035 | -43.18125 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36d09fdd-6205-3391-b4d7-dc9c06f37790 | -6.16694 | -43.33455 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44bd8698-5fe3-379f-b40f-e1ed55a44f38 | -6.20211 | -45.37204 | 2025-09-01 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe4569e0-0853-3ea0-8d40-2ea4912749b6 | -6.14984 | -44.14443 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f917be09-0bcd-3a6f-926a-fbebc1880968 | -6.30191 | -43.62445 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee9e68a3-ee44-31d4-9ca8-f562ff0153c5 | -6.46095 | -43.96299 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1caa2f8a-5d09-349a-85f0-f4ff77e63b4f | -6.86937 | -44.32529 | 2025-09-01 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8336410-5fc9-3032-b197-d902e10563df | -7.25151 | -44.24028 | 2025-09-01 03:42:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c3ae753-20d6-3626-93a1-58bdf9599ff9 | -3.4219 | -43.33389 | 2025-09-01 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c9da819-65e9-32cc-86fc-8d9b2ccd9cb9 | -6.19159 | -43.33871 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c87a3cd8-b5d8-3b91-bf7d-2d09655defb2 | -6.30132 | -43.30106 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af9b9948-fe3e-3456-85d7-29d3cd566abf | -7.07758 | -44.34114 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d472a70-8dab-3b1b-809f-157a607529cc | -4.64329 | -42.52067 | 2025-09-01 03:42:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4dbefe75-87e7-3f3c-9887-0127262ed2ef | -6.50917 | -43.55819 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01592db8-c140-3b37-886a-491d4e158e38 | -7.08959 | -44.33378 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 04007c7c-dd36-3df1-9cff-3984264b5f0e | -6.58005 | -43.71545 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e70c7638-a797-3e20-8237-faa0e6395783 | -6.82265 | -43.32975 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4dca9bd0-f8e6-3cd1-963d-8f103559602c | -7.10841 | -44.77501 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d694d28b-06f6-3937-aeec-8e9236d930f2 | -5.32921 | -42.86002 | 2025-09-01 03:42:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a544abdd-a3ce-31c1-84fe-ba2b31928312 | -6.52197 | -43.54734 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fedf10cb-579d-3721-985d-b45d2194621e | -6.45819 | -43.96393 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 732b7fbd-87ec-3014-9184-419c160fd705 | -5.1136 | -43.22667 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e4a983e-6d5b-3db6-abee-338640f15dc8 | -4.9149 | -43.18319 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afe91f1b-df59-3971-81b6-44b6a5013a52 | -6.449 | -43.97131 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4bb0c83-a867-3e94-892d-a3295bb7be7c | -5.31624 | -45.45281 | 2025-09-01 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab3edde-74bb-363c-b5c4-da2a45ba272d | -4.92487 | -43.18485 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afc2577e-f9d1-3821-810a-778fc3bf52a2 | -6.63595 | -43.95791 | 2025-09-01 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9768dbe9-e2ae-320c-8225-99c6e4614a83 | -7.08048 | -44.35498 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 5fd156c4-d628-3ba4-ba05-e030c0191f00 | -6.93192 | -42.01956 | 2025-09-01 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0583a998-875c-37e4-b007-70ba1618615a | -6.26393 | -43.54735 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d66c7ab5-a406-3a7c-9cf3-03ee617565d2 | -6.45873 | -43.9609 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bb529007-dd84-32ca-966b-6c99ed5e0182 | -5.56303 | -47.41233 | 2025-09-01 03:42:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37af3ea6-2a1f-302a-b057-6176a311eddf | -6.46198 | -43.95699 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 83117b39-db0d-3d59-b46a-223f40d02529 | -6.86993 | -44.32209 | 2025-09-01 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bd92311-a42d-3a08-b5e2-0f4e9d9594e1 | -6.30375 | -43.6157 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e5a7a0a-1204-3a95-8802-73096b2dee40 | -6.17517 | -44.12199 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7ffbe8e-4fac-3b2e-a876-2875b496169e | -6.1512 | -43.33746 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b00fd86e-97dd-3ec6-864a-06075f896857 | -7.11375 | -44.77599 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 895019ac-b6d9-35e0-9c76-47753f746b47 | -6.36985 | -43.55996 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73fe20e1-11e1-33ff-9eed-cbcecee0a9f2 | -6.71639 | -42.25411 | 2025-09-01 03:42:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e01f37f-18b3-34de-9d64-fd0cc835895e | -7.24636 | -44.23944 | 2025-09-01 03:42:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6b0357d-0412-36ac-ac66-2859f081332e | -6.28703 | -43.56253 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64a9a8c5-5ce5-3e0b-b557-5413a331e40d | -6.44741 | -43.94978 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2f1e55a-2ba9-3443-8ce3-a0bd9fab98e5 | -7.08795 | -44.34306 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2428abbf-93cb-3ca0-8b9b-ada27a481a94 | -6.58494 | -43.71707 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07b6bf68-b740-3519-a69c-19bd51966dbf | -3.60547 | -42.85821 | 2025-09-01 03:42:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 328b03e1-386e-3e7c-9601-772951fe332d | -7.09809 | -44.55915 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f820eb91-87e6-3169-9a95-c357c76235ca | -6.75749 | -43.79072 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b90cab48-8358-3e82-bd65-1701271251eb | -6.46147 | -43.95997 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a240d1a0-a02e-39a7-ba25-407cae4da79d | -6.64102 | -43.95898 | 2025-09-01 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 398adb4f-1fd8-316c-908b-8d5b4c7adda6 | -5.99546 | -43.36912 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f9637478-5da1-33e5-894e-29cdd34f4b49 | -6.50764 | -43.56717 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54f7997b-3144-3f5a-a5c8-04288d8d7585 | -6.29145 | -43.29973 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66451514-993a-325d-abf1-c3a2d93a87cf | -6.1995 | -45.37122 | 2025-09-01 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 694dc4cc-9a61-3df8-8012-a3287589470d | -6.37031 | -43.55727 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44b1a7cf-3c35-3dee-8616-299ba4d14e94 | -6.78318 | -44.62604 | 2025-09-01 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 664c7f33-e040-366e-92fc-9576581dd919 | -6.16492 | -43.31699 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 37881928-ebd4-3232-8daa-6294b99ce382 | -5.64251 | -43.65123 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50fb631a-7ab9-392e-8115-49f69fec2d8e | -6.45356 | -43.9603 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc66ddd-b5c1-3fc5-b888-5a9f2ddabe5e | -6.4467 | -43.96914 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93265546-f56c-30a3-9bd1-b8ce780b2c38 | -6.8005 | -45.69033 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29bce440-f1cd-3311-b17a-3e942377a056 | -6.1958 | -45.37488 | 2025-09-01 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b750387-6a2b-32bc-9a26-1edccd060b19 | -6.81395 | -43.35078 | 2025-09-01 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 381e30ff-14bc-315f-aa66-7d403dba7ca1 | -12.31253 | -45.67667 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4285d022-4583-3993-9c50-6927a93aa5ac | -11.01012 | -46.85292 | 2025-09-01 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cfb58f17-f733-352a-84d5-13ecfc2ff63b | -12.22208 | -43.88075 | 2025-09-01 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fd14fdfe-d1ed-328a-a8fe-b150ce4cfc82 | -12.57508 | -48.21105 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d79f2fe8-6153-3f9f-8567-46d4e706029a | -11.80354 | -44.94341 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README16.md)
