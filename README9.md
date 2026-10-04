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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73b96fc5-5709-3ed7-aa93-ad916eb50ba9 | -5.5469 | -45.259102 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef892f6a-e93f-3d5d-9e97-bdd8561fb59a | -5.85 | -55.715 | 2026-10-04 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7099b9-d82a-363a-a09e-61b7b90a7a42 | -0.4911 | -49.104401 | 2026-10-04 00:31:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a09918-c0f1-3efa-b615-42323ea619cc | -3.0831 | -49.530201 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4c0719d-ca0a-3706-b90f-772e4bf3a8f9 | -3.2726 | -43.384201 | 2026-10-04 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d51f0cad-83b5-3543-b85a-c52f7e8d19ee | -3.2856 | -53.8368 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90257fae-c264-3e35-8846-9a92248bdfd3 | -3.0358 | -54.228401 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec2d6df-eb91-3e2d-a72a-2e6c1271e302 | -3.2983 | -53.847801 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12383e9f-3574-341e-990c-6c3fc1d2da38 | -3.0716 | -49.525002 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaa729fa-c15a-3293-a61c-571c0edb382b | -5.5486 | -45.2663 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c10c4072-be49-33f1-9ede-fb7c9f756a49 | -1.4056 | -49.27 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bba65703-2b1c-3cb8-b112-635879c9b26f | -4.1526 | -47.5341 | 2026-10-04 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45c62361-8cd8-3a53-b12d-1275289bb2f3 | -3.5119 | -54.619999 | 2026-10-04 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2b87fa-97b0-34bc-b91a-f0c574d2f582 | 1.7788 | -55.6572 | 2026-10-04 00:31:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ecad315-4525-30de-8cfd-ce5c01070a75 | -2.8041 | -54.108101 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bff8a0b-c2e4-3c18-9b24-2aa1866593e5 | -3.0078 | -50.466999 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 400e5196-5088-3896-b404-59bbf54b3ed1 | -1.0892 | -54.0909 | 2026-10-04 00:31:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19424c64-8e31-3eef-ad09-8fe2ec6e6db9 | -3.27 | -53.812901 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea5b5fc6-de58-3e97-a3a9-c2cfec39f6f0 | -7.2703 | -49.251301 | 2026-10-04 00:31:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a52d8369-3fbe-3f07-8c48-526242e613b7 | -2.5727 | -51.858799 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b90ba83-4370-3f95-bda0-d12a96273ac8 | -3.0847 | -49.537701 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95ff1a09-1c20-3c79-96b5-bd254e0e1150 | -3.0883 | -51.094601 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7e006df-629d-3dec-a42d-86d2583fe600 | -4.9237 | -45.686501 | 2026-10-04 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d481168-66cd-3df4-abfb-dbceff54731e | -3.1102 | -53.739601 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8abdd7-003c-3d27-8b34-ecaaac3420a6 | -4.1332 | -46.820801 | 2026-10-04 00:31:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd7c983-684e-3424-b748-e7daf997304c | -4.2904 | -50.27 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3167ea2-1908-3c1d-af84-c68dbef4b9ca | -3.4691 | -50.0961 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e98505a-f350-3ec4-b736-6ae7f22971aa | -1.1556 | -49.258598 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f100daf-bc5c-3f5e-9675-75a791ae7de4 | -4.9852 | -46.041599 | 2026-10-04 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8cce11-ba71-3fdd-85b1-ae1b6af7e198 | -2.2128 | -53.712299 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44095bcb-d2cd-3427-89b7-8bd7af039225 | -4.8063 | -45.313801 | 2026-10-04 00:31:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c67ddc37-4cae-39e4-925c-bb8ef435cdc6 | -3.177 | -50.5326 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7394b1d3-c6d5-3609-ae24-b3655663349e | -1.404 | -49.262901 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 918462e2-2209-3584-b046-d724b8257ffc | -2.5792 | -51.887402 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 428d2bae-c5ab-319a-8507-490bdf4d7d61 | -6.5768 | -44.143799 | 2026-10-04 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67e7e99c-174a-30e4-bf32-e32c595a082c | -3.0634 | -49.534599 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f44de2-d60f-3318-972b-e68f65d46aa5 | -2.2357 | -51.913101 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ea44e0-5fb6-338e-ba1e-a9010b9cfe59 | -3.5752 | -55.316399 | 2026-10-04 00:31:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68fcb2e2-70e4-30c7-8cde-52b94148495e | -2.6804 | -54.422401 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58684aa5-7740-34a9-a7b6-d79953cf45dc | -4.2588 | -46.380798 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4b2533d-bf0e-36b5-a379-022c38db4981 | -4.4485 | -50.9725 | 2026-10-04 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ece86921-cba9-3cd8-acaf-de1242479835 | -2.8882 | -54.117901 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22526de3-c1f8-3659-93e5-34dcc631cc53 | -4.5168 | -45.890099 | 2026-10-04 00:31:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9338bf8-d0d6-3f5f-9132-2a21143e6359 | -1.417 | -49.274899 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08df1645-ae1e-3a87-a85a-49582c614dfe | -4.2825 | -50.2803 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8e595ef-abc4-31b1-b4e1-528526a915ec | -5.5502 | -45.273499 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a132f715-46a2-37e6-87c9-2908fbf4c72b | -5.8688 | -43.590801 | 2026-10-04 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c33657b-5505-342d-b4e6-3f26ddadd95a | -1.092 | -54.1035 | 2026-10-04 00:31:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbcf869b-79ed-3824-8f72-abca68de2d80 | -14.5597 | -52.8876 | 2026-10-04 00:31:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f51efba4-5377-3592-ba54-afd48925f49e | -2.2378 | -51.9226 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3084e944-85d3-3b8a-9cb2-ee2c5f2c1bff | -3.0749 | -49.539799 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 474bbf1a-3134-32c9-be72-be24d99fab62 | -5.7419 | -43.271801 | 2026-10-04 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91a1a982-5868-3cd3-9a22-63b3c767ac5e | -4.4853 | -45.531101 | 2026-10-04 00:31:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 562a6b7e-5b23-3830-adf5-e706b4ccd639 | -3.7736 | -51.3978 | 2026-10-04 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d899ade0-6092-38cd-b705-76288306d79e | -4.0208 | -44.820099 | 2026-10-04 00:31:00 | METOP-C | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a939962-22a9-32a5-bd8a-725beec54bf5 | -8.0342 | -47.061901 | 2026-10-04 00:31:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee8e6f92-a168-33db-a478-d2b103fde5a5 | -4.9253 | -45.693501 | 2026-10-04 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9accfd7-8adc-39dd-bd07-834c8d8546a0 | -4.252 | -50.783901 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3048c684-c2b0-373d-87eb-337e9650ac4e | -3.8905 | -49.684399 | 2026-10-04 00:31:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc86dbf1-c889-3329-a3ae-89e8dc839a58 | -6.8179 | -46.6548 | 2026-10-04 00:31:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c93a392b-8d8c-3486-a1ce-aba5d0d8d922 | -6.5688 | -44.153801 | 2026-10-04 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc4b57a1-bde8-33f6-ac41-c8b735e18c8c | -2.5847 | -51.866199 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f70c024-e228-3fac-9275-fcc773ab1bf2 | -3.7578 | -49.553902 | 2026-10-04 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1596ca1-abd5-3faa-8911-37e932d4686d | -3.464 | -44.334599 | 2026-10-04 00:31:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e854a67-f994-3876-8231-ec2e0abb7ee7 | -3.8709 | -49.688801 | 2026-10-04 00:31:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0a9786b-8284-3e6d-ae59-dab8f15e3917 | -8.54 | -50.073399 | 2026-10-04 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03acdbd6-d04d-3adc-b508-3170d8c18ea0 | -3.1869 | -54.0811 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec6e1fc7-e901-30c6-8e6c-8e4d2a5c8f2e | -4.1232 | -54.1535 | 2026-10-04 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd37601-4464-346e-bdee-d1cd9c9d675c | -6.0085 | -53.5313 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a40c2902-2f71-37ef-bff6-7ca0a2f9bdbf | -15.2524 | -40.524899 | 2026-10-04 00:31:00 | METOP-C | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19a2f091-e203-3ef9-8e22-997912812dd6 | -3.7613 | -49.569099 | 2026-10-04 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26ec3685-ca51-3352-8bf7-a3b5d9a6d8ee | -2.5804 | -51.847099 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf8fa4a-b5d5-3fd2-a580-39877c38c693 | -3.1801 | -54.096699 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8301e3fd-70e1-35a3-8318-a3a55b9ee835 | -3.353 | -43.375301 | 2026-10-04 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9830d5df-a0d2-3fd4-b949-0d0d693ff033 | -3.0766 | -49.547298 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2d303e5-8bab-3ffb-8e76-9a55e945150d | -3.4575 | -50.090401 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3aa32f3-c969-304b-941f-a37858c522e6 | -2.5923 | -51.8545 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93eae209-8e4f-3dbe-aa0c-26b73207be2e | -2.943 | -54.134201 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e20d9c9-28fa-3a07-97b7-70442f009d48 | -6.5786 | -44.151501 | 2026-10-04 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a12a80f-ab7b-36f7-8392-018ffad87b75 | -4.2708 | -50.2743 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ebc014-50b6-3666-b5fa-948e530cc05e | -3.0327 | -54.214699 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce214141-6414-3225-a5d6-fcf921814ad4 | 2.3473 | -50.750301 | 2026-10-04 00:31:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7817e22a-4f0e-358c-b869-1dd6a240b719 | -6.575 | -44.136101 | 2026-10-04 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc39f0d-61a3-3c33-8ab6-f4f9a85795d2 | -3.2827 | -53.823799 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a6fe52-4420-349e-847a-420f68fb07fc | -2.3592 | -50.602001 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 901c0062-b310-33d2-ad89-1c2da65dea7e | -3.367 | -43.391201 | 2026-10-04 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e224261d-2e43-3a83-8683-04a022b4d86c | -2.8199 | -54.132801 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9c1e85-bd6a-3178-a143-c9c03b41f170 | 0.8404 | -51.2467 | 2026-10-04 00:31:00 | METOP-C | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2729c771-2aa3-3410-b343-cde60857225b | -4.1495 | -49.691799 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd879d08-f6cd-321d-a7c5-f8af4086e82d | -2.6904 | -49.0289 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68afbf75-22f0-3ffc-955a-394731b7bf6d | -2.8135 | -46.778702 | 2026-10-04 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7278c160-9002-3718-b8c3-192870001261 | -2.7846 | -54.1124 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e80f179f-cfb0-39f8-8adb-d78d498d8687 | -4.195 | -53.464001 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73a8c02e-9a9c-3f0f-ac38-a5c20cbbcf5b | -3.1821 | -44.584801 | 2026-10-04 00:31:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc14ffcc-4a8b-3855-bfee-6c4d3996e960 | -1.4874 | -49.447102 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd8f7116-09b3-3744-83b4-d4c73afbdd67 | -4.5314 | -49.696999 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 431b311b-549c-33ac-824c-d1a573c52ebd | -3.0651 | -49.542 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98a536b9-1317-3c2a-88b4-838ca4259c84 | -1.4842 | -49.4781 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59476d66-36b1-35ab-b59a-3fe3068ff248 | -3.4593 | -50.098301 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32da6a05-4d52-3d04-9ecb-aace2f0490e5 | -3.1789 | -50.540798 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
