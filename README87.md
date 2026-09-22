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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c1b0232-2b62-3197-a591-7a50d13169b9 | -7.08475 | -61.08807 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a43592d-32e0-3797-a1c1-e4885ef1e330 | -6.72554 | -55.09442 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91a67dbe-3a5b-3392-a7cd-865a3dd4b92f | -6.7489 | -59.46663 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0e56b7c-73f0-377b-b748-e83f2989b461 | -2.95437 | -57.72221 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1da08b70-5e38-36ca-825e-e304536193bc | -3.29779 | -57.86374 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e7cb2d7-3049-3d52-8edc-bd67a1e979df | -6.69516 | -60.01153 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a4acd2f-c2b0-3735-9424-09c05f6cd126 | -3.17145 | -51.35742 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c934d5e-13a7-3c3b-82ff-2ad5eb48da79 | -5.27726 | -49.33965 | 2026-09-22 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1f0ffff-ce56-343a-aff2-4ec574b28a47 | -3.22466 | -53.9492 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dbc7d1f8-e08f-358c-b083-aac62cdd6a61 | -11.24126 | -54.11127 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a0b3d50-b28f-3db5-b811-432d51a2a304 | -6.46001 | -60.03604 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad6ed580-416c-3a03-bd1d-10055ebe542a | -2.56894 | -57.50942 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4a07859-c126-3315-b23e-ebb878e149df | -5.93515 | -59.97866 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e08554-b9fa-3fbd-8640-e6c3de0a6b06 | -3.47425 | -59.58918 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9447adea-dbe2-363d-b329-cbd0ffa62f2d | -6.11051 | -57.64058 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89a9a4dc-6233-3109-a0b1-21c48280929e | -3.40191 | -59.42482 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f56f1cc0-d4ea-34a8-a899-61b1d5c7bee9 | -2.17017 | -47.88485 | 2026-09-22 05:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dea029f-9293-32a5-bd30-e71e1cbcb854 | -5.84696 | -53.55093 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b58f0263-e824-3a7e-b733-349f4ad6bc13 | -12.86589 | -50.94116 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6bb47ae1-cc35-3691-b754-91417b3fcb89 | -6.71018 | -58.99728 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 324da2eb-4123-350d-91e6-8860ca4d2c4f | -4.2225 | -48.61765 | 2026-09-22 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bbdd1284-408c-3ff8-97c1-ad403d4e658e | -10.9002 | -53.96523 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56567bbd-43a7-3b05-9187-53b560a1298b | -7.87145 | -54.73434 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 629d5e07-1ac4-335c-b88d-24b936242087 | -4.52011 | -55.75608 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8a35a4-cc03-33cb-94e5-e67ce9b4adb3 | -5.93961 | -53.52633 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 031f26f6-f034-353c-b1e4-55bd92c38b42 | -7.59033 | -57.67299 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fe50c1e-1b26-34a5-bf5a-258a331a04f3 | -6.09331 | -57.62001 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9fb2e203-93f3-3f45-a238-468c2c9ec2ce | -11.69393 | -50.98742 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 27eac90f-5fb6-357b-889e-c2f80833e76c | -7.5931 | -57.677 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eef86169-540a-3188-9d44-f402785b56a7 | -10.9531 | -54.36722 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45e4f752-0ff2-3d9e-921f-3e6227846e67 | -6.09997 | -57.62107 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a723a80b-4dc3-349b-9499-ba71fcb6af87 | -10.90538 | -54.06591 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aff610fd-4e99-3269-9f9c-27f46a7b0da1 | -3.44441 | -50.61696 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f1f1f09-d398-3775-8a90-b3fb88877528 | -6.28095 | -59.91877 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf65a257-8e2a-3f0c-a28a-111afd72e898 | -2.56615 | -57.50537 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c49e238-d723-36dc-9fa7-94cd4a06ece2 | -3.14625 | -58.63881 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c57a306-ed12-38d2-abbe-87e027378834 | -6.67122 | -50.94464 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 086cc8ff-3b6e-3efc-aaa4-081fbab1a2aa | -5.87151 | -53.64083 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 650466e5-1b75-373a-9555-55e17b2ed6bc | -7.24767 | -55.58129 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b64feaca-3d1f-3298-a3c4-ba7e16ab4e8d | -6.42646 | -59.97782 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de59b3cf-ac26-39e8-bbf8-fd73372fd50e | -6.81744 | -58.98103 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6d0f325-11cd-351d-b95a-0a9b1c1d0b4a | -12.02194 | -47.81316 | 2026-09-22 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad506f69-7c4b-3e3f-aebf-f4585c82664e | -6.12146 | -59.94751 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d946fc4-0527-36f7-a10b-041c34a58138 | -7.38937 | -51.77314 | 2026-09-22 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa8f0efd-165e-316e-817e-16de201f33d6 | -2.53085 | -57.55404 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fb7dcd2-4d75-3e28-bb94-675d1b816015 | -4.27955 | -56.25959 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad5e71a0-af7e-3171-96e3-90459cd43e57 | -2.92617 | -57.79058 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a432e2ac-c7c5-3f2c-9b4e-7a9316d072ad | -3.30453 | -57.8648 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25795940-bde8-3b41-8b1e-b44c2eb4bcb0 | -5.80683 | -57.74547 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f411e51b-6384-3e72-b454-33ea8623025c | -6.07312 | -55.61672 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b57618d-a447-3864-b8c1-493d68be990a | -6.62273 | -59.92344 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| a508aac5-1e91-3937-b6d8-e43c8fd1a2cd | -7.56871 | -57.68025 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dac1e176-58cc-30a8-9d56-ed383ecf8125 | -6.70958 | -59.00092 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1895fa21-8d4c-3f63-b2da-b2ba41c16bdf | -7.85783 | -54.70275 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87f9573d-ffa4-3c48-92fc-1f71d03b3330 | -6.73259 | -55.07184 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e152ec-ea5f-3db5-adf0-512bbc0d4938 | -3.48248 | -59.5727 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1eed472-8736-3c2c-a641-f8511bbaf8d9 | -6.19084 | -57.77459 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f18f28c4-df00-3bf0-96e3-5efcc84b5f26 | -3.45066 | -50.60528 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6499d7a3-431e-36ff-989c-1d5667120cc0 | -3.15194 | -60.64614 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b10852de-bb69-3718-a1c1-a3d50ad3ffb8 | -6.65903 | -50.93411 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7db0abd7-2d07-34c0-b396-c43b2279077b | -12.79809 | -54.06096 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fbee89d-5e43-3175-9594-c4a7c60dd1bc | -3.33133 | -59.81063 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33519c23-fe6a-3faf-a796-37ed18dfe37d | -4.27137 | -55.44609 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7073d26c-def8-3f7c-afdc-f06deff0d234 | -3.38591 | -50.4408 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cc347b5-9ccc-3d69-8fae-aa4c75ec4e2c | -5.98456 | -57.70982 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e6d57ea-2d15-3915-8b2b-a1c3622f6618 | -4.27871 | -55.44355 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51c02152-14bb-3840-b721-2623442e4235 | -4.30969 | -55.59935 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a3510ab-9335-3d42-ad9c-4dfb59a9dfc0 | -3.68441 | -42.96242 | 2026-09-22 05:23:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d21e861a-d924-385f-b931-5f533c1d429c | -3.41435 | -61.2946 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52a04645-eb93-30dc-b263-e7097ac8f43f | -13.33278 | -51.28674 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6d9b91e-0ce1-3f08-bbdf-95498e39f2e5 | -4.22139 | -63.07753 | 2026-09-22 05:23:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e77e8955-2777-3927-8617-c87d38abfd60 | -8.11545 | -49.58365 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5708a84-4ee1-3b5f-8976-b9c63331751d | -6.61634 | -59.91835 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 367f34cb-456f-3215-a97d-696dc9a2d2ab | -7.23674 | -55.58348 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04793805-cf36-381b-ad2e-275d94b7997a | -4.48144 | -55.48635 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a39fbe1-3a90-3c74-a50d-5b2aeab8e013 | -5.45248 | -60.14531 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93d82eaa-c83c-3d79-94e4-340921ead1a3 | -3.3132 | -59.44072 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35614160-57b2-3b24-a635-cae5660c9673 | -6.11109 | -57.74409 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06b786b3-8b25-3c21-b26f-807d3c963800 | -7.33181 | -55.59762 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3ae589f7-21c8-38b4-a3fe-07bc003605f1 | -3.01379 | -54.19118 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d77fc9b-1541-3662-8d34-fc5d87cf59a0 | -12.68113 | -50.96534 | 2026-09-22 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99605487-9617-30df-bc4b-9cafadf37104 | -3.79999 | -51.35984 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2757bff3-b43b-3759-bccd-9be018fa9d36 | -3.24177 | -53.95596 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c8ebf42-4e9f-3f6d-8903-5a8dd9dc0134 | -7.39732 | -55.22121 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e8bf2d9-fda6-3aaa-b7af-f9ff6b12ab95 | -3.36375 | -61.28854 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85ce7c54-b17b-3f58-b2ed-0394bb1d354a | -6.06995 | -57.87344 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dcb42a7-6685-32ee-8584-988f5d777d56 | -6.52704 | -55.36135 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 360dc8bd-fa3e-3ea3-a7c7-c214b960c60c | -3.89779 | -60.59243 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0e9f24f-ff52-3b56-b915-7d3bcd15649d | -6.78659 | -48.67924 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf4c008-3326-3a71-9f05-24d3a595a011 | -5.72967 | -53.46227 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a21c224-b5c9-3c0e-90b1-7b62480e33f2 | -6.06946 | -57.72675 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c276db4-36c0-3f2b-9871-9d5b5f01849c | -11.95174 | -46.51579 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4fe4b7a-81a9-38f1-b40b-91f6359fb4ce | -11.80078 | -49.80883 | 2026-09-22 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3a2c1ac-a88c-3674-bea8-ffd50fdfe411 | -3.52996 | -58.65973 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bed426b9-b8af-3c9b-9ca9-e4de7a571ac8 | -3.63206 | -58.91845 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7536cb6-10d0-3253-998f-f2f580036f09 | -6.0605 | -57.86835 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59ce17f5-2a83-38f3-8284-198438ed0260 | -12.84945 | -54.04198 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f634fb4b-8da1-335f-bea6-27c79a9790cb | -4.87271 | -55.83992 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abedc198-18cd-3304-b7cb-17b9d60baffe | -6.06971 | -55.61618 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80360637-ac2c-3060-88c1-0cff5975f04b | -3.37164 | -61.28982 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README88.md)
