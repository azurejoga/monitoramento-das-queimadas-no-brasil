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
| bfe3694e-418b-3672-9cf3-1a93d794d7bb | -6.94758 | -44.55679 | 2025-08-10 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 51d30109-18c1-3c29-8f68-e66e38ffca17 | -6.6762 | -44.73387 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f93f811d-dbcc-386d-aa90-7c863324dcfd | -7.36532 | -46.65794 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc0f6f1b-25bb-3174-ba28-6837b6312f10 | -7.88195 | -45.55793 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43a5dde4-3cd2-3f46-a590-0f788b21c137 | -8.06553 | -49.71283 | 2025-08-10 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53aad990-031a-3a04-89e6-9e808d2052d3 | -4.30455 | -48.07823 | 2025-08-10 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1820ea1-4ebf-3486-ad3f-9a92c9497c30 | -7.49317 | -44.89555 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acbb26a6-8d21-34dc-b7e8-b3319663d6ec | -4.29771 | -48.0724 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18d76e1d-8c04-3273-8d40-7850c88fa681 | -10.34612 | -44.90811 | 2025-08-10 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 154f352f-03ee-35d2-8730-bd1f8e7eabb4 | -8.50063 | -44.75246 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6ee1c8f-9784-30a3-8dd7-e849b57480aa | -7.59813 | -44.42049 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58fbd631-79d9-3498-9b84-4b7243dacbcd | -10.23632 | -45.30831 | 2025-08-10 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f11df1-723f-3756-92cd-2a94c3de141c | -5.85251 | -42.95389 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 90825ec4-4198-3e29-a344-42a5ce5b3468 | -5.20897 | -45.61856 | 2025-08-10 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae1d4a17-eb49-399f-a03c-07a674b07199 | -9.64168 | -48.34292 | 2025-08-10 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9730235f-235c-353b-9ebf-810ef7cb2884 | -6.22509 | -48.45073 | 2025-08-10 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6183845c-0eb2-3ef5-a655-1490afa0e798 | -7.87862 | -45.5574 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0ee9089-f6b4-357e-9a57-2fd41702514f | -6.83326 | -44.31779 | 2025-08-10 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8abe80a-7e16-36e3-9807-338e1c2f4a10 | -8.49954 | -44.75943 | 2025-08-10 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3e17e68-f800-30a6-972a-ca678592cc51 | -6.98062 | -44.80029 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87bba4f3-c3bf-3f0b-851c-d2cfe82b5606 | -5.66725 | -51.31208 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd660d13-a981-3649-beca-807003520aa2 | -7.73355 | -45.5159 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86b58f0f-e0da-36b2-a913-44a545378285 | -6.56482 | -42.8405 | 2025-08-10 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f1c7a30c-f54c-3ba3-83b6-534c58e91e6b | -9.49236 | -46.30243 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78c45495-2df8-3990-b822-24a35f1c7b6c | -9.49245 | -46.28055 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a914b9e9-2339-3a69-bcd9-af3b6a317052 | -9.52824 | -45.39874 | 2025-08-10 04:21:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0aa8573-e2ca-3e34-893b-93b81d223b2e | -8.10733 | -47.44021 | 2025-08-10 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6376c08e-da85-343d-82b3-377733125753 | -6.57994 | -44.57305 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3e9c30f-7375-3b4d-b295-b803ef4443cb | -9.49294 | -46.29888 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56a8b12b-ec6d-3e57-8f2b-f5cf949e6f13 | -5.3904 | -41.3227 | 2025-08-10 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80b88dfd-8c37-3e9e-9069-903e071b4fa2 | -7.27874 | -44.58014 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 563a038a-2d72-3f2c-ba66-6c5bd83c2151 | -4.3003 | -48.07497 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed972378-3e56-3cb5-949c-080e14284355 | -10.43798 | -48.34654 | 2025-08-10 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab0b473f-9ce3-34cc-8018-867cc507cd16 | -3.83995 | -47.75109 | 2025-08-10 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c4ada9d-74c8-346b-b089-9497f9d63479 | -7.22014 | -35.77662 | 2025-08-10 04:21:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c63b0c87-35b5-318c-8968-7313f74eb532 | -7.87472 | -45.56038 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eaa7bfc-9608-396f-9f31-1fded9fa1232 | -8.09905 | -48.87622 | 2025-08-10 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2cc62c4-cdda-3a79-ba2f-652e040d9d8a | -10.45424 | -44.38643 | 2025-08-10 04:21:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe502aea-fa13-365c-b84c-495fb7190c80 | -8.11213 | -47.43296 | 2025-08-10 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cdcf7cc-5f59-3d64-9adf-4bef33b8acdc | -7.72743 | -45.53289 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcdfeeac-314b-337b-9813-2da52d1a266b | -6.18798 | -45.4424 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 574011f5-9a34-3157-848b-de1d03245e1a | -8.30226 | -44.99892 | 2025-08-10 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84a3f48b-9133-395a-bc9a-655daf5ada47 | -6.98394 | -44.80081 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d8efe9d-0e72-3d64-b4cc-b139808e4583 | -8.07485 | -46.85514 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32218349-ba33-3e45-9e54-13cd43d05f01 | -8.49731 | -44.75193 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4399577a-f732-3d5f-83fa-53d46888ab4c | -10.46183 | -47.94413 | 2025-08-10 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c1892ea-4a99-36e7-abde-2e65d9ce4b6e | -7.73021 | -45.53694 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f179863c-d3a8-350a-828d-a4e3473ef9f9 | -9.7658 | -48.58561 | 2025-08-10 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86e51f74-2faf-3926-baca-310771309753 | -7.59533 | -44.41998 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82c93a11-4463-3cf0-9b11-239f4fa1d537 | -5.47641 | -44.70337 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52e31a61-7930-3eb9-992d-623da6417f03 | -7.1594 | -44.06891 | 2025-08-10 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21df603e-1d17-3d61-b984-e69017ec3575 | -5.41104 | -44.4306 | 2025-08-10 04:21:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c7ddaae-91ee-384f-8342-04d06958433d | -8.05439 | -44.79226 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72be41b8-38ca-3c8c-ad91-9bad93b56373 | -11.77901 | -44.95686 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ee44c63-713e-3113-9776-6b9567b1e5a0 | -3.96467 | -47.88463 | 2025-08-10 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 069fb3b4-8240-3371-8fba-3947d7641f6f | -7.72965 | -45.54045 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ccd11bf-5a0e-39c2-ab9a-1064700eb220 | -7.41171 | -43.99285 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 804daad2-333b-3211-84de-e3929f5fe295 | -6.41115 | -44.56722 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5130453c-0539-3d4e-b5be-108310f2f97a | -6.96182 | -44.48795 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 901440f6-f5f5-332e-9833-9635f2389ba9 | -7.08992 | -45.61851 | 2025-08-10 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749a3770-2ec3-3445-8d87-10fee76acb70 | -6.95199 | -44.55043 | 2025-08-10 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4d3a3307-bedd-37ea-9276-50104c373f49 | -11.75337 | -44.9454 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93a60fcd-a353-37da-a140-863454f63f93 | -11.7318 | -45.01865 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2d6fa49-1832-3c80-b3e9-1e3d758fee55 | -6.9509 | -44.55731 | 2025-08-10 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ea7a230f-a0e0-32c3-8abc-809f8ac2ba5b | -7.88251 | -45.55444 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9802a30a-cfd6-3812-99c3-decc2a4821c7 | -9.86755 | -44.70267 | 2025-08-10 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bd59ce63-3137-38ac-9fab-9c408c93e767 | -7.53926 | -44.00193 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e788bd3-fbf5-3172-a12c-bde13c887c3c | -4.29953 | -48.07955 | 2025-08-10 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4469d51-2788-31c1-82bf-99331d9e37fc | -8.07428 | -46.85509 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb08e8d3-88a2-3a30-956e-0d32ae8d788e | -6.34267 | -55.56248 | 2025-08-10 04:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 656521d8-26f2-3299-9ca4-0026e5f5d726 | -9.52879 | -45.39524 | 2025-08-10 04:21:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 544de8ec-31c3-3030-9ffc-6c6fac34275d | -9.52492 | -45.3982 | 2025-08-10 04:21:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| be8e3db2-6747-3c10-ac83-4fd8aaeb9466 | -5.46977 | -44.70232 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 230462c3-f9ed-333f-96ca-ccafb0048add | -10.34279 | -44.90758 | 2025-08-10 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b41db6e6-85e9-3308-83bf-6872f66c035a | -6.98126 | -43.95446 | 2025-08-10 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d3d35eb-98d4-3328-82fa-62c111878eda | -4.1454 | -46.451 | 2025-08-10 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a6fffb1-e2c6-36ef-b362-ecb49bde265f | -8.50118 | -44.74897 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c797244-395d-3b57-97fb-44bf49553822 | -9.51995 | -45.42963 | 2025-08-10 04:21:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab9c5f29-b377-3351-b927-28074d0ea90e | -4.07459 | -47.97052 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0be2b00c-b0dd-3676-9487-3bac73d62198 | -11.74795 | -45.02485 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fe2abcc-9c9b-3d66-8ac7-38907e4b6525 | -7.27488 | -44.58308 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18cae634-42c3-3791-b4c6-fa8499236801 | -6.99497 | -45.6218 | 2025-08-10 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c5567c0-025f-3da4-9a6a-905dd04ec2ed | -6.21542 | -41.40428 | 2025-08-10 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1de60dbe-e9e8-38e5-a5b7-07c329fcc199 | -11.77956 | -44.95329 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b22dbc64-3a24-31fd-a5d3-e5f630361253 | -6.60901 | -43.38935 | 2025-08-10 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6440d04a-609f-3f09-b2b1-428616abc210 | -7.34682 | -44.60157 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fc5ad70-f4d8-3ed4-b69f-bab41cdc96f8 | -6.27371 | -43.70108 | 2025-08-10 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efe42531-2824-3a92-bc6e-7d9605646de3 | -7.26668 | -44.63514 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f531015-9848-3666-b638-9a9b8352d445 | -7.87806 | -45.5609 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83111736-496a-3431-b351-11ac75a6b369 | -9.52437 | -45.40169 | 2025-08-10 04:21:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29e46e83-8a14-3626-a71e-696d5b56b445 | -4.30106 | -48.07039 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b39d1d27-a3db-38b7-abae-0d411dc1da3d | -7.42896 | -43.99195 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96001f28-f868-399c-9971-40e92efcfcaa | -7.27323 | -44.16553 | 2025-08-10 04:21:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00ea6531-fff9-3361-8ba6-ce841dacb9c8 | -6.16931 | -44.40877 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45c4a6b7-be64-32c1-9478-0ab20538e6ba | -6.05587 | -43.7528 | 2025-08-10 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18b17b57-b953-31fb-8f39-2a7796dfa31c | -11.05257 | -43.26742 | 2025-08-10 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a48f8dbc-2f93-319e-af1b-f77894bff631 | -6.97939 | -43.85695 | 2025-08-10 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b8bd1b4-caed-354b-830c-2a448b5703a0 | -6.96514 | -44.48848 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fcb38087-5271-3551-a69b-befffaa272b8 | -5.82388 | -44.10551 | 2025-08-10 04:21:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f44741-4b6a-3575-a070-61a9edf4ee24 | -7.69911 | -45.53906 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README16.md)
