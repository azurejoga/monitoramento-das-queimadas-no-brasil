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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6da6fd32-2291-3a65-9b6a-faefda5ef041 | -11.3989 | -46.3759 | 2026-08-20 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 5a99c8d7-edb6-33c5-87a8-446074a78df7 | -6.4481 | -60.0676 | 2026-08-20 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 22377b75-3e4a-37da-8312-9078c68233ac | -11.1936 | -54.0199 | 2026-08-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 35b132fe-ef51-357b-a143-7b4467f96b23 | -5.8087 | -55.7293 | 2026-08-20 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| ab28ca13-fdad-3e43-96e3-962a493a2679 | -10.8451 | -50.3081 | 2026-08-20 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| cbbd5bc8-56c7-3769-84b6-3ceb7377dd12 | -10.3897 | -61.2118 | 2026-08-20 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 36a903b2-8b6c-378a-a057-ab7d33938a1b | -11.1939 | -53.9993 | 2026-08-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.7 |
| fbeef1d3-7bbc-3dc3-945b-cfae4fe06a7f | -10.8265 | -50.2887 | 2026-08-20 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| bc121ccc-ae09-3411-8e20-9be0918c4193 | -9.2071 | -59.771 | 2026-08-20 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f7a1c240-ee0f-36aa-9033-96164822c8a8 | -6.2353 | -55.4118 | 2026-08-20 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| eab7e9e5-e2fc-33f0-85db-a910cbba81b1 | -8.3104 | -46.5095 | 2026-08-20 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 99c84552-48a8-3f8e-937a-0d0604fffd9c | -9.1901 | -49.9604 | 2026-08-20 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c826bfd6-6f6f-375a-9dbe-5889123cc7e3 | -8.3292 | -46.5077 | 2026-08-20 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 173a231e-8150-3800-97e0-a3adc4c11e5d | -7.022 | -45.8878 | 2026-08-20 13:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9513c61c-ebc4-3c80-95a4-e9bf392da1f6 | -5.7904 | -55.7103 | 2026-08-20 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| fef2864f-d0cc-3a88-9aa9-b1b13de1f913 | -7.4615 | -45.1484 | 2026-08-20 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 41e72249-adf6-3856-890d-1f06470f6deb | -10.3898 | -61.1925 | 2026-08-20 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2f0c1f2f-21ea-340e-baef-88e8d23de066 | -11.3797 | -46.3784 | 2026-08-20 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 5d23dd2e-5e4b-34db-9cb0-caf10b52aba6 | -11.5812 | -50.5476 | 2026-08-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 130b475b-97d7-3807-b443-a4fb805c7666 | -6.4481 | -60.0676 | 2026-08-20 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b5b81668-c906-377e-9d22-f331cf5bce96 | -5.7903 | -55.7301 | 2026-08-20 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 68ab914f-4abf-3d1e-90a4-f38c84047092 | -9.2258 | -59.77 | 2026-08-20 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 0cef0238-b657-3980-a235-464a02ad97b4 | -6.6014 | -58.9844 | 2026-08-20 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 25448177-de04-3fc7-a90c-473ac920590e | -11.8377 | -58.8445 | 2026-08-20 13:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8b6b5a12-b707-3fd4-8610-3e07242bf2b9 | -6.583 | -58.9658 | 2026-08-20 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 3f0fdcc5-42aa-32c8-8ba1-c7f4cfd923e6 | -5.8088 | -55.7095 | 2026-08-20 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| cb68d0b9-9482-35ff-9cd6-8e7982481c56 | -9.4257 | -60.416 | 2026-08-20 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6c87c28b-2ab6-313d-82ac-d2d24755628d | -6.4391 | -52.7343 | 2026-08-20 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 246.7 |
| f8749aa2-41f6-3c9f-92a0-805dc223edc6 | -15.7151 | -47.8036 | 2026-08-20 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d74e7a15-329c-3d69-878c-4987ca947c32 | -18.0285 | -44.6113 | 2026-08-20 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 0f06e5a1-d87c-3aa1-975b-94f2974697d1 | -11.3989 | -46.3759 | 2026-08-20 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 336.8 |
| d46e4320-bf8c-3eb6-953c-01bcb12498c2 | -11.1936 | -54.0199 | 2026-08-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 163.3 |
| adb9cace-534e-3b00-b8d9-c17ac7755782 | -9.2071 | -59.771 | 2026-08-20 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| b16ebdcf-17a3-3b48-ac24-1f5e29ac139c | -11.3985 | -46.3985 | 2026-08-20 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 3a1880d9-2951-3b28-9f4b-b6e372d44dd5 | -11.2125 | -54.0181 | 2026-08-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 229e6764-328f-35bc-a34e-893474c51467 | -5.8087 | -55.7293 | 2026-08-20 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 35b9ded8-d974-313e-afed-745e91e58bbd | -11.2189 | -55.0585 | 2026-08-20 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 726065b1-66e0-31b3-bf2b-ff04292c6797 | -19.6632 | -45.8952 | 2026-08-20 13:40:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 8e851bfa-ea47-3b28-ae0b-29af5fa3d667 | -10.8265 | -50.2887 | 2026-08-20 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2034bd7c-65bd-32d7-ab75-3150cc84e2a8 | -6.2353 | -55.4118 | 2026-08-20 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 3db84798-1f08-31c7-87a3-40474fde5ca3 | -10.4084 | -61.2108 | 2026-08-20 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e34eaa97-6f59-3aa6-aa3b-8b7e8497d398 | -11.2128 | -53.9976 | 2026-08-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 308a0d91-d4f0-317c-be3b-b49b82440ab7 | -11.4227 | -47.2486 | 2026-08-20 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b93d89ee-dcf8-3b2f-af96-8595bc80d0bd | -6.4392 | -52.7138 | 2026-08-20 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 96643d05-c3f2-380d-8ee5-15cda750a93b | -11.5815 | -50.5261 | 2026-08-20 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| fb295251-1f88-338d-b6dc-32e1dd78e2fb | -11.1939 | -53.9993 | 2026-08-20 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 262.8 |
| e3281abf-c2b6-3d5e-a640-d44e1900e39c | -10.3897 | -61.2118 | 2026-08-20 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 440b4492-74a7-34dc-a6d2-d8c2ee667390 | -10.4085 | -61.1915 | 2026-08-20 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9088b898-2090-3956-a150-bb1b9fa038c7 | -11.3985 | -46.3985 | 2026-08-20 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 79400165-07fe-38bf-ad8e-1f63c95e4c82 | -6.4392 | -52.7138 | 2026-08-20 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 225.7 |
| 04c921cf-5569-3138-8f15-effdd8137b62 | -10.4085 | -61.1915 | 2026-08-20 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 57e82c8f-4aa1-3bab-b4b4-1c062646431c | -7.344 | -55.6741 | 2026-08-20 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 47d8e23f-b580-3b0a-8d98-de55a9eadf5a | -9.2071 | -59.771 | 2026-08-20 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 14cf6647-56e8-3b62-a026-ea8958b88e95 | -7.022 | -45.8878 | 2026-08-20 13:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 83405a0f-5cc1-3223-869c-00288623dfe8 | -10.3897 | -61.2118 | 2026-08-20 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| f192af0c-7359-338e-a650-690748d52920 | -22.7788 | -47.533 | 2026-08-20 13:50:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.6 |
| 48f0fe7e-cf18-385a-ab57-a204f750cf80 | -6.6015 | -58.9651 | 2026-08-20 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| cfa6bccb-a845-38dd-9ef3-e01c7fb908fb | -11.3989 | -46.3759 | 2026-08-20 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 258.3 |
| 8bfed8e3-3c53-37f4-89b5-6a6a92e0a95a | -18.0285 | -44.6113 | 2026-08-20 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 285acbef-cd88-35cd-ad7b-2d4dbbf62787 | -6.4481 | -60.0676 | 2026-08-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fad9637f-921a-3ec0-aa0c-2ac675c0d478 | -9.4257 | -60.416 | 2026-08-20 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 27288377-fdf0-3aa7-ba6d-3613207573d5 | -11.4418 | -47.2461 | 2026-08-20 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| de966445-4b0c-385e-bdad-54c535890887 | -8.3292 | -46.5077 | 2026-08-20 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9a12a41a-ff3b-3faf-bfe6-c7f666cd5a97 | -11.1936 | -54.0199 | 2026-08-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 7cc02687-32a4-3627-a017-6e5e14de6869 | -9.2258 | -59.77 | 2026-08-20 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a9129733-353b-31bc-8916-2c0771076952 | -19.5213 | -46.6147 | 2026-08-20 13:50:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 8e933521-903b-3b53-84d2-283876d7fe6d | -11.8377 | -58.8445 | 2026-08-20 13:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 49de6036-3f4b-395f-9481-a8bfc62434cd | -11.2128 | -53.9976 | 2026-08-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 67885b57-9bad-35ee-8d79-1db8748a2633 | -11.1939 | -53.9993 | 2026-08-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 262.4 |
| 48b47e2a-0fc1-3e3d-a8bd-3ce4f9afcd4c | -6.2353 | -55.4118 | 2026-08-20 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 566a4f45-91d7-3016-83ce-5dbc0739082a | -10.3898 | -61.1925 | 2026-08-20 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| f60c7ab2-bc8e-3c9a-9894-308887c16fc4 | -5.8088 | -55.7095 | 2026-08-20 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 531daa08-41ec-33b9-8c92-7296e1d25919 | -6.167 | -45.235 | 2026-08-20 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 8ec74b9f-06ac-3d8a-88b6-325c72e04216 | -5.8087 | -55.7293 | 2026-08-20 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 3377702a-8a70-3a63-8077-8e26a9487945 | -5.7903 | -55.7301 | 2026-08-20 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 51a7ab23-5d8a-306e-bbed-1253bb2dff0d | -6.4391 | -52.7343 | 2026-08-20 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 466.6 |
| 5bb290f5-3c26-32cb-8fca-17dccd67efc4 | -11.3797 | -46.3784 | 2026-08-20 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| d8a43e82-ffa3-3e93-937d-4dedf59de51e | -6.583 | -58.9658 | 2026-08-20 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 469d216e-bcd2-384c-bbbe-e503788d9e45 | -17.4418 | -44.912 | 2026-08-20 13:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 524.6 |
| 3557c5bc-7bf1-39c6-ba78-5e918a245f96 | -6.6014 | -58.9844 | 2026-08-20 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 440b2e21-c7f7-3c08-9058-6442a270c3d0 | -6.1668 | -45.2576 | 2026-08-20 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| c9849150-2c20-3917-aba4-12e23f52a888 | -19.6632 | -45.8952 | 2026-08-20 13:50:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 031599a4-4dc9-3ef0-989c-be7bf39df56f | -6.4389 | -52.7548 | 2026-08-20 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 53d451b6-463f-3777-b111-5b3c149601ac | -15.7151 | -47.8036 | 2026-08-20 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 728f136d-3b50-3d54-9ae8-05340ee51459 | -11.2189 | -55.0585 | 2026-08-20 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 514fa6eb-54b2-36d3-840c-a2bfa11d20ba | -5.7904 | -55.7103 | 2026-08-20 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 4590d7ec-d59c-36e5-9199-d969e19e6915 | -6.4576 | -52.7332 | 2026-08-20 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2880558d-7fc1-3db5-ad37-4ce81b44eb0c | -22.7796 | -47.509 | 2026-08-20 13:50:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.4 |
| 14c64c8b-f174-3b58-9501-dc74e18b66eb | -10.4084 | -61.2108 | 2026-08-20 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 45a9da8b-67c0-3bbc-aba1-686cc2f136fc | -11.4227 | -47.2486 | 2026-08-20 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 180.7 |
| f034ddcd-b7c7-34fe-bd22-b277858b038b | -19.5213 | -46.6147 | 2026-08-20 14:00:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 259.9 |
| d27d5f5c-f1bc-3dfa-8bb7-2996ec7401a7 | -10.3897 | -61.2118 | 2026-08-20 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 6b28169f-6e84-3e00-8120-891c850c5603 | -11.2125 | -54.0181 | 2026-08-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 9bef394f-09a0-3dae-a269-5f362a060dba | -6.4576 | -52.7332 | 2026-08-20 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f4dd913f-992b-3947-aa15-92557e7a6f6a | -22.7796 | -47.509 | 2026-08-20 14:00:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.2 |
| e33b04bd-1848-36eb-a3ed-35a565a25d25 | -9.2258 | -59.77 | 2026-08-20 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a6727c68-0ef1-3647-9287-75f777991e55 | -7.022 | -45.8878 | 2026-08-20 14:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 97eee140-e4dc-3457-a091-14251717457e | -18.0285 | -44.6113 | 2026-08-20 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 43ffaa3a-c04c-3b2d-887a-f4911a5b50b5 | -8.3104 | -46.5095 | 2026-08-20 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 85ad21a4-ae82-3d85-8e47-f6fc613abb05 | -19.6632 | -45.8952 | 2026-08-20 14:00:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |


[Clique aqui para ver as próximas entradas](README73.md)
