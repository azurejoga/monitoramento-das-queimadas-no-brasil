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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf900d5a-c7f9-3991-a2f2-c37ddb82fa3c | -13.47622 | -47.22798 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ae375cc-8b1e-36c0-b279-4f359ac6a2d7 | -13.38292 | -47.55081 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59b4f230-d6a0-30b0-a032-f0b501ce52d4 | -11.50132 | -54.46108 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a64b0847-6c24-35e5-b26b-71a280c3b0ed | -12.22781 | -47.83728 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79aa513b-283c-34ef-8797-a75e2425bbd4 | -13.35871 | -47.20614 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ae8b0f5-e3d1-3309-b005-42993e0730ca | -11.22379 | -54.86622 | 2025-10-05 04:46:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79b8d221-6a3b-3a40-a963-1fc391de31da | -11.92909 | -46.44788 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd9c0239-13d3-3d05-8959-fb8f923a805b | -13.48543 | -47.2832 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a257b9c6-1599-34be-8990-4addd0ac6762 | -13.57111 | -48.16704 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 51cf54bd-eaf7-3de6-b9be-e1550548a3c9 | -13.08285 | -47.90693 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d098c1c4-1eb4-336d-815e-bd0f2ee0b7fd | -6.76432 | -42.23987 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 71ce81eb-6772-3949-86a3-ae0e0b5144f3 | -12.9871 | -51.00939 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dac8ade-2175-32f7-895d-e462987bd40d | -12.98372 | -51.00885 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64516323-46dd-37ac-b205-e3a1576b57f5 | -11.80889 | -46.84873 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e2ff20af-a834-358b-9a11-640ef0f79462 | -10.61873 | -48.67186 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72b75e21-564b-3434-a7e6-5575767ed34c | -13.13332 | -50.87294 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e34f1651-e04f-3021-b092-80334cc8a8ba | -10.70007 | -47.98986 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45bffbec-0672-3958-bc1b-8e724e08506e | -11.30856 | -49.99339 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36e99657-7a61-34da-a164-1edb001e05b0 | -11.45258 | -51.51482 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98221935-2c38-3d93-9633-1d3480d3b010 | -10.3604 | -43.73724 | 2025-10-05 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e67fa1a-a407-3a68-aefc-7b53d76bf8ec | -11.93308 | -49.92253 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56097dcc-0b14-3b32-8825-2b3d9c30b0e2 | -10.46379 | -57.50267 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 06e8e916-11cd-34b8-88c2-e469f14632e2 | -11.22028 | -54.8656 | 2025-10-05 04:46:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b15bc86-0779-3a7e-b3b6-1cd0ec19554a | -13.30172 | -48.09271 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ba5c15d1-8bdd-34bc-9ee0-77895f7249fd | -11.03124 | -45.57727 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0824d46-a8c0-3816-963c-22ce5cf42f32 | -7.7424 | -42.61368 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45432a11-f2d6-3fae-bb56-70c1d51ca5d0 | -10.9903 | -46.66282 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef3ba4f8-48d6-3285-8c20-317e552d4405 | -11.95526 | -51.49625 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17289343-2fc5-31cf-881b-60662971f1a2 | -12.94318 | -51.01443 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28bbbe63-761b-3b2d-bf58-b64e6d416c37 | -8.58083 | -46.33027 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ad5321db-ab25-30a0-a3f5-22fcc6767195 | -12.18828 | -46.57389 | 2025-10-05 04:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a361bbe-261d-3371-952b-ce57567e6f54 | -10.73048 | -47.64679 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 652b02c1-ac2f-3b7a-bf4e-8d30c0c023ba | -12.40826 | -51.09274 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d97c694-a567-3e01-957e-b7c49e9e91fe | -13.28653 | -47.61681 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72281448-7ec4-386a-a41d-701a8885b331 | -13.59992 | -48.16831 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97456ac3-ab35-30c1-b2a7-f4092b4db829 | -11.6325 | -45.07662 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f05aa64-5551-34bc-a698-778989fbf6d4 | -10.46508 | -57.49517 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9946f657-4e30-3e3e-92b4-2c29691f437c | -9.80371 | -56.17036 | 2025-10-05 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8db092c5-bb4b-3e31-8f08-35c863286e58 | -13.34845 | -47.59451 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15b1ee37-4439-371a-9fce-13da177b8cc4 | -9.95614 | -43.77758 | 2025-10-05 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ea3f2a5-742f-30ba-9ce4-53478dd8efa8 | -7.77392 | -42.61525 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e824cbe0-ec0d-3265-80d9-893f75a37fef | -13.25216 | -47.22612 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee6a0155-482d-3073-95d7-1b5b87248478 | -8.53861 | -46.30611 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db2bbc9e-d99f-31ac-939c-381ee4771ff3 | -11.09754 | -49.85597 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a66effee-a60a-3601-b9cf-d8cfa1028420 | -12.70337 | -45.85911 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4c53356-7933-39bf-9919-a5154b3b1c8c | -13.08426 | -47.89634 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ded9f206-7bd3-3cd6-9225-ecb39178296a | -6.40351 | -47.29315 | 2025-10-05 04:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46377bd9-eb14-35eb-83d7-d6a9e35e02fb | -10.34816 | -48.15748 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30cf3387-409c-33d3-b8a7-6e247f4ffe0f | -7.47313 | -42.62894 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb75b6af-9bef-372a-972f-d65bc3d6d178 | -13.3321 | -48.10243 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8d8f39d-1d38-3c36-85c0-574fe34bedd6 | -10.01294 | -48.28226 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fc1c0c4-b4e5-3d4b-86f9-6ee2f5af402f | -11.30519 | -53.96457 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaf82a8d-76a6-33c0-9825-cba0cef3ec9c | -11.09868 | -49.84823 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a0dd940-2169-3229-8b89-1d80a10a1bfb | -8.74818 | -48.61003 | 2025-10-05 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ad79af-bb30-3ff6-95fa-46784f3c807f | -13.34149 | -48.06314 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b045f650-167b-31d9-b13c-bcce221e440c | -13.09735 | -47.82815 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b8257b98-23f8-3e75-a661-205c32292303 | -7.78578 | -48.43702 | 2025-10-05 04:46:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72b9d945-24e4-3cc4-bdd8-1fb38e40ef0c | -9.78772 | -46.77054 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da07f45f-dc6f-3767-b8aa-981dae7fc98c | -6.63658 | -47.76469 | 2025-10-05 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23bd4993-c95a-36b1-902c-3197b3ad6e4b | -13.3471 | -47.57392 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77678e36-2ff2-3784-be4e-dafd1ca0b20a | -11.69754 | -47.49958 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bbe0f33-b6d4-3ab5-b1b9-06db30ea65c6 | -13.25579 | -47.23018 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c893d469-ab35-3c67-8089-d7ba7c87de9d | -13.1012 | -47.85919 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ed1c590-84b9-333f-8f42-e85dd4bc1d86 | -8.6135 | -54.97407 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3af5edd7-1eb2-3aad-bbe5-88eea3452281 | -13.09656 | -47.83701 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a676ec50-744b-3e88-99fe-04c44694476f | -9.38861 | -46.52983 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ee2fc82-ffd8-38b9-8486-b7f10ce0d045 | -13.49856 | -47.27893 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb59c7ab-e7a7-3901-9765-d943bb509350 | -6.98532 | -44.21437 | 2025-10-05 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5832d05d-619b-30af-969f-aab16a0856c5 | -6.61538 | -43.71883 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdaa05fa-ba1c-3cae-95d1-93230e0e3100 | -8.61127 | -54.9649 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef9127d6-5d31-3124-ae4d-bb1387b3976a | -9.46894 | -45.53598 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e8fd427-3ff1-3006-bc03-8bfd5c9ff4d7 | -7.77529 | -42.61516 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 95c8652a-3154-36e2-9021-4bd7fe7f0b85 | -11.12402 | -47.75803 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bab513c-9817-3260-b81b-e53c3f803379 | -15.20853 | -56.82807 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d554957-9c04-330a-92ab-6144e559deab | -14.60891 | -52.5261 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 121914d6-b3eb-3312-a260-d40075067b3a | -14.69634 | -48.34505 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c758bf8e-117f-3f0f-8954-24a64b02d01e | -17.8853 | -57.63577 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 298620cc-abd7-341c-9cec-d6d14770406c | -14.88194 | -48.15777 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85c27d39-ef86-3066-b46b-698d961f6d64 | -17.11445 | -48.92859 | 2025-10-05 04:49:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02fa7572-cafd-327b-8dc5-074793592bec | -14.6918 | -48.34927 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f984a747-a1f8-3e2d-8d16-03363c632da3 | -15.61322 | -52.49545 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 940d83ac-1bac-35d8-9390-3c3cc6ebb818 | -13.74674 | -47.96817 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80043fcf-66bd-36ec-88af-29f06417ca6b | -19.59173 | -44.62975 | 2025-10-05 04:49:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14c7abae-9098-3cc7-a089-df2e9f9fa962 | -12.90242 | -54.75219 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7eba2200-05dc-314b-b73d-2f023a56bb72 | -17.9297 | -57.60122 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 62a69013-fa94-33de-8438-de33268bca12 | -15.31487 | -47.32033 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f184680-5260-3b93-94af-d5382f273866 | -14.68661 | -48.35828 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 89cb99bb-2570-3de8-820b-59db0c6a5608 | -18.20486 | -53.37273 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31800f8d-0d98-3213-8a65-50a09cb8b338 | -13.72976 | -51.26765 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47a330db-c322-326d-b742-dd01b8a11311 | -17.90006 | -57.6388 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 81446eb6-92c6-31bf-92fb-97b10b70f759 | -15.29996 | -59.23883 | 2025-10-05 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d935c59e-194c-3736-960e-d86554a03c32 | -15.97956 | -50.85865 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d73a1d4c-f007-3d4c-aaba-0578d83932c9 | -18.24015 | -53.3639 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d513f229-8840-3b7c-9348-f6c9a61cb3ad | -18.24737 | -53.33909 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ace6f501-1ec6-3f2a-977d-6798b0484ba5 | -16.34866 | -51.47077 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd822c51-fd98-331b-8e33-6d206f8d1490 | -15.33551 | -46.30207 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08d0e50f-3627-3b4f-8ec9-835423a529fa | -16.0147 | -50.95768 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 26fe8aca-9298-3b5e-8379-74597f31138c | -16.83827 | -49.34627 | 2025-10-05 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17027bba-ba99-300f-9dff-240e4e0f30db | -15.37775 | -47.94031 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a48880fc-45cc-3651-90ca-4e11accf7ead | -18.17788 | -53.34969 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README104.md)
