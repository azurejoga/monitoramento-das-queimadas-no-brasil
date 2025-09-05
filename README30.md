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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4df20c3d-4b4e-3ca1-ae7f-d032c4efbb21 | -10.99016 | -45.92939 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ee185b8-4abe-343f-a3cd-cb50fc04c13f | -12.94423 | -48.0558 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 053d6029-7226-30a9-b612-116a6d9c8608 | -10.74444 | -46.34177 | 2025-09-05 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 705ba0ee-2116-3be0-8077-bc634ed85d5f | -10.97212 | -45.97691 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b80ff04c-1066-3c16-9273-b50fce502d07 | -11.00015 | -47.15921 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 481eade0-5dcf-383a-a478-2fab5e72b38c | -10.22734 | -50.54084 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23131df2-13a0-3a52-8a52-8a58f6e800e1 | -11.00754 | -47.15656 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab5596d-a217-3891-9c1a-bdfcb580a3aa | -8.20579 | -49.59123 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75f5db2e-90db-3ad9-9ab1-00dfdf63b22b | -11.094 | -45.12208 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9099fab-aae7-3c07-b6cf-bbc5441a8663 | -8.89769 | -45.77668 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40bacc53-0d3c-3b60-889d-a05a4103e8d7 | -8.36549 | -52.55251 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2a4f79e-3f2a-3c64-a722-90115d07db2f | -9.0772 | -47.00958 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 93fe2cda-da35-34c3-ab5e-ff513ab10f5d | -11.54465 | -47.314 | 2025-09-05 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cd0c38d-b3d6-3195-9734-ad8f1fc9bc72 | -11.64247 | -54.5402 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c53da10-ecaf-380e-8f9c-e75e990772d5 | -12.97658 | -48.07526 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78a7be49-543c-3b31-8ad4-1d07e29759b3 | -9.70381 | -48.98985 | 2025-09-05 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 602959fa-a392-39ad-b112-4b8214b9e720 | -12.29242 | -50.00466 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63debf62-78ac-3c63-bb94-9f1e2fad3065 | -10.96558 | -45.97178 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c6f2410-dead-3769-8deb-f1d8bd9f9b8a | -8.00937 | -45.44205 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 724a403a-5726-3551-817c-593bb2072bcc | -9.98303 | -51.62271 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ffdcc14-d246-3cec-8e5d-941b3022104a | -11.19914 | -55.00818 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4846eafa-9db9-3f05-9321-2aa82d96f7c7 | -11.91644 | -46.64261 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e820d0e-cbbe-3a1b-96f3-c3f05fffd6ce | -13.00534 | -45.22687 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 709cf4ad-3a53-31e7-b27e-0b44d2ad103e | -10.99368 | -49.76598 | 2025-09-05 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90bfc9a8-2c44-3dd6-b20f-74f9b14ae2ab | -11.65404 | -46.85925 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20cc6006-e93c-36e6-9f53-7b72106f0f24 | -8.02189 | -45.40713 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cb29f90-50e5-3d7e-ac47-0c6e956d8382 | -7.05569 | -50.8656 | 2025-09-05 04:36:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3eae318-ef13-37fd-9cf5-ebd25b3e22b6 | -12.87373 | -48.01181 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d11a953d-9867-3f4e-9a34-ebec34a1ecbb | -11.65062 | -54.51829 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7015ca78-889f-3026-9709-c41ebad849a6 | -11.02486 | -45.06761 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 408edf3f-cb04-3c7c-a005-e59f302814b9 | -12.71539 | -45.08072 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bf73fa40-5543-3bb1-a0c5-f6fd4d4043fd | -7.72063 | -50.32566 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ef3a049-fda9-3f71-aefd-1a399446ae58 | -6.84944 | -52.80494 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13e1d73c-0e6d-3e56-bd61-fb7ec66a3deb | -7.61695 | -47.94609 | 2025-09-05 04:36:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99b05c81-0aa1-37e0-84d8-1bbe2a1ab68f | -10.07268 | -48.06681 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0413e6d7-e9b4-350a-af1d-303c79681612 | -7.79945 | -52.13138 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1adfb989-be39-3446-8e92-627f620a27d7 | -9.70052 | -48.96768 | 2025-09-05 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c999cf9-18c2-31c4-970a-b5859f2a12cf | -7.6903 | -50.29284 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e28e79bd-9bac-3fc2-a544-62ce9df17f0e | -8.00522 | -45.4455 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbf1a009-225c-3dca-8707-231812f76af5 | -9.97737 | -51.63451 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1f0dd28-1628-32aa-86ba-b9750f7e7222 | -9.42 | -46.79893 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c03d74b-398e-3cc6-aa7b-fb863364c3fb | -12.97878 | -48.06083 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed3ff23d-6b0e-3315-9621-c03c6979ae5f | -12.88172 | -48.01248 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 271aca03-9869-36ed-bccf-ca42b4559fa5 | -11.86225 | -51.44162 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82f07edc-eb70-3161-978b-ad16d4fb2cd5 | -10.97997 | -45.94872 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 804540bb-b0fd-3096-a9e6-67abd11ff82e | -11.39261 | -43.60662 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2bba676-7444-3d6f-a675-0620ce745dc6 | -13.46988 | -46.83926 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5c84ebf-feea-35d1-9041-687d6cb35e5d | -12.48954 | -48.08861 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fe6a268-052e-3e1f-9501-79f42567c08c | -10.72632 | -47.94845 | 2025-09-05 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18867df5-37f2-35eb-aee1-00bcc9b9ac16 | -11.54749 | -47.31824 | 2025-09-05 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5649802-4e64-3aff-b9c4-7837b35f3ce6 | -12.50145 | -53.84861 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92cde481-c938-3d40-9c2f-aab159f8983a | -12.86415 | -48.00661 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94d13dea-95df-3afe-a986-806caeca62c5 | -12.88116 | -48.01615 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bfc3425-c731-3968-b603-35cda5703741 | -8.88171 | -47.92521 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4f7df14-1f8f-396f-bcf4-49e4fda7a8b3 | -10.97518 | -45.95632 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d93a06ed-fe4a-3f2d-aef2-030c94e89396 | -11.03295 | -52.04869 | 2025-09-05 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e13a8e9b-392f-3a79-ba6d-40014312fd57 | -11.62946 | -52.21308 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8bd6b00-d82f-3067-9cf6-d1c630ea9c8e | -8.90063 | -45.78122 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21074a24-2150-312c-b223-a1c7c1389a17 | -7.97816 | -46.33858 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1aaec486-453e-3d41-836a-7d7b5108b17d | -11.0934 | -52.0224 | 2025-09-05 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10f9e696-5548-3064-9326-dd78160a238d | -9.51124 | -57.81776 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba6e98ab-bae3-3a25-8ba9-4152544e3281 | -12.50224 | -44.75812 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf9dbe2d-0fd7-3695-971d-48c5b2720c80 | -8.19048 | -49.5999 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3c1ce28-8fce-3efe-8a6b-eba4724b6941 | -11.54806 | -47.31452 | 2025-09-05 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76354a4c-65e6-3a1b-8d58-d50c6633e811 | -12.93017 | -48.05735 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd971ce8-6ddd-393a-8c07-80f1fa5dd46a | -12.98271 | -48.05766 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df6287f8-17d0-3cf4-be4a-cc0054b2ec65 | -8.35428 | -52.5435 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cf7bcf5-e1c8-38da-9b62-ade90707ed97 | -11.68609 | -52.20816 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97b7665a-d0c3-312d-b77f-d88b5f988363 | -11.77186 | -50.65172 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca9b7614-d8c7-3b45-a8a5-2d61f0c107e5 | -9.06986 | -47.01221 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f009f49-2876-3c10-a29b-0fe7c855d1e3 | -11.98465 | -40.86032 | 2025-09-05 04:36:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecffb79b-227d-36f3-9371-8d80ba62bdbc | -10.87872 | -55.39332 | 2025-09-05 04:36:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 729e2773-75f5-3092-8d79-41979057cc7a | -8.22035 | -50.04184 | 2025-09-05 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa36ba6c-fa05-31ff-869c-78455c9c2dfc | -12.91213 | -48.03976 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89943939-052d-32e9-983d-d88377410384 | -12.91661 | -48.03302 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9601a77b-6c04-3131-b836-1fc07fe4c5ec | -8.90003 | -45.78524 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12fd3239-9b11-3ce8-8983-6b64edff8fe9 | -9.49385 | -57.82171 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90271ae0-a6bb-33a9-af59-7abc1fc5fe8b | -8.97563 | -44.4512 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae2c88b0-6674-354c-91fb-e0242d37267d | -10.03527 | -48.13689 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0ec068b-3381-31fd-b72e-1fa143fb33c7 | -10.06061 | -58.38762 | 2025-09-05 04:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d9a90e7-8390-300e-9a10-de7c9cbea8aa | -13.00914 | -45.22744 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| da8526e3-dc95-3ab6-9d25-c774012aaa09 | -8.44557 | -45.03749 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b865a57-0b84-3c02-9e9d-2f1cc8703b0b | -9.98371 | -51.61864 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12c9beb4-5b7a-3db1-afed-9009f5cb306b | -8.49883 | -44.63403 | 2025-09-05 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a028573-2d5a-33dc-b5c5-ab21f307760c | -12.90029 | -48.02678 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 127b9860-5dcd-3190-9bfa-6cf5b3b33983 | -11.26499 | -48.33534 | 2025-09-05 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 973c573b-2420-33b0-ba95-2a28e143ae7b | -11.61248 | -47.78522 | 2025-09-05 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0057ed46-9612-3ba3-9dae-9438d6544846 | -12.18372 | -53.90066 | 2025-09-05 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f226e296-7f8a-3e71-ac78-9025335f940e | -11.62072 | -52.19842 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fce0cddc-7dcf-3e4d-921d-3ba9cea9ca03 | -12.24354 | -50.13673 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89a5658b-03b8-38fe-b85b-a93d4f73e1d4 | -11.99918 | -46.74264 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69e3c3d1-733f-3479-af19-0d1cb01bfb1a | -8.34806 | -48.30553 | 2025-09-05 04:36:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aac0f9a-c041-3603-a2e1-99143ef68d59 | -11.93108 | -46.66461 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2740f97e-0672-3ee5-8873-6dbc6e11756c | -9.06309 | -47.01118 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bedba3a8-da5d-359a-af96-990288fb4e50 | -10.97223 | -49.76302 | 2025-09-05 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8558cd39-067a-32cb-af71-b336d5494520 | -8.09477 | -45.33543 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 393db3a7-4a0f-3655-9259-8edfef1f304a | -11.63309 | -52.21372 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 313a7025-d0f8-30fd-bc2e-74392736dcbc | -11.20271 | -55.01308 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1a201c1-d5e6-3826-baba-f9916e6b3b00 | -9.05941 | -50.44183 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65ba1b89-d85f-30c7-8494-c9e101d5d300 | -11.19839 | -55.01233 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README31.md)
