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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11e7508a-38a2-3b61-a71b-bbac38d074c8 | -14.9247 | -45.5403 | 2025-08-25 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| dc6ffa16-3a0f-30d6-80f6-940ff347a746 | -6.8063 | -58.6275 | 2025-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4c8d0588-0377-3458-9760-a23ab1ac9606 | -8.1119 | -62.877 | 2025-08-25 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b6722048-8aea-363d-b03d-c80bcb6e0be1 | -7.6326 | -62.7243 | 2025-08-25 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| cd1ea3f3-9073-31b2-af5e-470de1aefa58 | -6.8202 | -59.4194 | 2025-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7e72beea-be1e-3043-b9ca-787d2611e91a | -3.4439 | -49.051 | 2025-08-25 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| b932ed28-7196-3bc0-8a78-85140bd05e61 | -3.4254 | -49.0517 | 2025-08-25 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| a1e7fb14-6043-32e5-bbae-7e38503eae9c | -5.118 | -43.2198 | 2025-08-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 220.2 |
| a3a148f2-0ea3-3e05-aa7c-96ffa1ce74a2 | -8.2313 | -61.3922 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 222baf10-57dc-369b-95ea-b6026df18572 | -5.4364 | -60.1779 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 400cf209-01f2-3a95-9945-3e0fbd59a5b6 | -5.0992 | -43.2211 | 2025-08-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| da6a6d43-2f52-370a-b985-b9ea1d2b1955 | -5.0994 | -43.1977 | 2025-08-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| d0802ddf-62f7-3864-9d46-0145ee433f53 | -10.5937 | -44.331 | 2025-08-25 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4e0a34a6-3034-3cec-a3b8-1f68edc85cd0 | -7.6141 | -62.7249 | 2025-08-25 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 653e7099-e661-3102-98be-cce6fc9f7224 | -10.4239 | -64.4281 | 2025-08-25 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 20c26ef4-e928-35e1-a74f-626d218cfd53 | -9.1722 | -59.4629 | 2025-08-25 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f50b00c3-ed5a-3e47-871b-b7b3db2aff5d | -9.8101 | -64.2642 | 2025-08-25 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 047caba8-363d-35ce-9d30-bd1b9ee0d08e | -5.3078 | -60.2008 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 883cbbc7-7b19-3861-a4c7-a4e82dd72adb | -8.2314 | -61.3732 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 04c9e035-5ea2-3718-8e84-a863531c7abf | -6.8062 | -58.6469 | 2025-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 7e8dd974-e60b-37ce-bff9-456093d96ff3 | -8.8733 | -62.4685 | 2025-08-25 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 3f232bad-4521-3612-a1ba-69a162a6ac19 | -9.1988 | -60.9274 | 2025-08-25 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 58674b22-beb8-34b0-9c49-d8184ad294ae | -9.2174 | -60.9265 | 2025-08-25 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| be47d015-5648-33b5-8fdc-cd1c40a998b9 | -8.8734 | -62.4495 | 2025-08-25 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 3f1a35f9-15f0-3d25-ac21-3652d2a23c4c | -9.1909 | -59.4619 | 2025-08-25 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 1108e52a-391c-3e42-ab5e-f0e4a5855b09 | -6.7878 | -58.6477 | 2025-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ead252ab-e28d-30a1-887a-182a104e86b3 | -8.8919 | -62.4487 | 2025-08-25 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| ab16343f-eaaa-35b3-987e-23ef75e9cd01 | -5.1181 | -43.1964 | 2025-08-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 4a2e614c-d343-34f2-af92-e703007b346d | -6.8201 | -59.4386 | 2025-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| ec95f9b3-074c-317d-b475-67ef28f1736e | -20.0507 | -44.4738 | 2025-08-25 00:00:00 | GOES-19 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| 4cd6e502-d713-3ff0-9a14-727b9ae42d5a | -5.4365 | -60.1588 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b6d71e06-1bf4-37db-8e1a-a438d99c1c12 | -8.5458 | -48.8592 | 2025-08-25 00:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1472d2d3-c26d-3a0c-bb24-9af0a41442b5 | -5.4181 | -60.1784 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5b6ae43d-2181-340b-a084-9f7b132379dc | -8.2128 | -61.393 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c70aa6ef-2ced-364b-aa8d-7a2b036d9d17 | -3.8383 | -55.9774 | 2025-08-25 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9d186470-2b4b-38b1-bdca-dd5a83ba376d | -8.8918 | -62.4677 | 2025-08-25 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 19811f23-5581-3635-bceb-01d799621623 | -6.7879 | -58.6283 | 2025-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 09b2d3f3-c26d-3464-b350-a637321e9a08 | -5.4182 | -60.1593 | 2025-08-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3ab7a210-7c7b-3a48-b777-78622ee44d2e | -3.4254 | -49.0517 | 2025-08-25 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| b35d9f0b-0f62-3001-9769-2a752c226321 | -9.1988 | -60.9274 | 2025-08-25 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 36ded09a-612f-34b9-96b8-12ae9f744d9f | -6.8005 | -59.6511 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7d088d11-cc57-30f0-8e3c-d77117b1048a | -10.6128 | -44.3284 | 2025-08-25 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| fd39604a-e954-3961-ba92-f21310a8fd6a | -5.4181 | -60.1784 | 2025-08-25 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7f06bb79-d76c-3adc-81b4-2268e9bf3e14 | -6.7879 | -58.6283 | 2025-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7138a6ed-d97d-3aa9-bcb7-fb6d17422a56 | -10.0232 | -51.0712 | 2025-08-25 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6a5ce2e3-3519-3a1f-813f-32734c54cf7b | -8.2128 | -61.393 | 2025-08-25 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f9b86400-147f-34f9-b3d6-1496e5045dd2 | -9.1909 | -59.4619 | 2025-08-25 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b68f8347-3e26-3b15-87c2-ecfe6968d212 | -7.6141 | -62.7249 | 2025-08-25 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 89691df7-25dd-3546-8a4e-b48eceaf73c0 | -5.3078 | -60.2008 | 2025-08-25 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 37293f68-6430-3d5e-b882-f02629970f38 | -8.546 | -48.8376 | 2025-08-25 00:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9e942918-9e8a-3cd5-b5f8-f1b771114de3 | -5.0994 | -43.1977 | 2025-08-25 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 189.0 |
| d2a6caee-246b-3a42-bb0c-c1701c775b37 | -10.4239 | -64.4281 | 2025-08-25 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 7a706c2d-01b5-3f4d-9414-cd929c7fb7dc | -5.4364 | -60.1779 | 2025-08-25 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| db0df41a-b9f6-380e-b7f4-a5c2705f317f | -20.5898 | -51.4131 | 2025-08-25 00:10:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 189.6 |
| 6d32a8c0-1935-3f06-bd17-7d0880815154 | -6.7635 | -59.6718 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 9bb8f930-a709-3b20-b46b-4c475c97d653 | -8.8919 | -62.4487 | 2025-08-25 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 866dbfba-c0b0-34f2-ac5e-68848dfef1ee | -5.118 | -43.2198 | 2025-08-25 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 4288eb6a-e15f-335f-a806-f8e818074f81 | -6.7636 | -59.6526 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 2d867f58-8d6d-3df2-8b6f-b49d24b2a86a | -18.0799 | -51.3908 | 2025-08-25 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 526afee1-e909-3fdd-ba43-91ddb131810d | -8.1119 | -62.877 | 2025-08-25 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3f81db22-8d6b-382d-8eae-88e5fdefac5a | -6.7819 | -59.6711 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| ece3e5b8-0fa8-3c6e-8411-0506841db7a6 | -6.7878 | -58.6477 | 2025-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 85125bf5-254f-39c3-a91c-6b372a63c171 | -6.8062 | -58.6469 | 2025-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d64b5214-bcde-361b-8006-89a0f1382be4 | -6.782 | -59.6519 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 207.7 |
| 88be82e0-b427-3879-8ecb-a0ab297c7791 | -3.4439 | -49.051 | 2025-08-25 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| db4d4b05-c6e9-3bd0-b1c8-65415c670695 | -6.7821 | -59.6326 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0d9e74f9-2492-34cd-92e6-304b274a65ec | -6.8063 | -58.6275 | 2025-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d52299c0-7d95-3134-8394-598dc417081d | -6.8202 | -59.4194 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fd64a8d7-d099-3ece-813b-7c0971a9c4ab | -8.5458 | -48.8592 | 2025-08-25 00:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 02ab5891-4c4e-3977-b9a4-6665d3c40dc5 | -10.5937 | -44.331 | 2025-08-25 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2287510b-b67e-3d9d-862a-2ea20142c78d | -7.6326 | -62.7243 | 2025-08-25 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 217fcbd2-975b-32c5-a0da-243bc1bfce51 | -9.1722 | -59.4629 | 2025-08-25 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2c42f1e7-88f7-330f-bb28-e111febfce27 | -8.8918 | -62.4677 | 2025-08-25 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 40201b35-a604-32eb-a186-7d8f5eab0727 | -5.0992 | -43.2211 | 2025-08-25 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 258.6 |
| a81d0988-a04f-345e-b89b-7f817d8fd825 | -9.8101 | -64.2642 | 2025-08-25 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 600e8254-23f7-3fae-801b-741f1505ef82 | -18.0599 | -51.3942 | 2025-08-25 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6e043f6b-96e0-3bf4-8b2f-2e77c9e25fa7 | -6.8201 | -59.4386 | 2025-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 81d6e563-57f6-3b9c-bd48-397328c3754a | -5.4182 | -60.1593 | 2025-08-25 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d6888499-427d-3b1e-8225-85f0dcbb54b5 | -20.6102 | -51.4091 | 2025-08-25 00:10:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 55b1da22-ea57-3147-bd8a-599cf670edad | -8.2313 | -61.3922 | 2025-08-25 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3a45c9c7-38ed-317e-9627-b3f9fd2f6ad6 | -5.1181 | -43.1964 | 2025-08-25 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c5a99c40-8936-3277-9039-4e09e632eb15 | -20.5904 | -51.3907 | 2025-08-25 00:10:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 239.8 |
| 2768db74-86f5-30a5-a7e8-e267a5b15629 | -20.6108 | -51.3867 | 2025-08-25 00:10:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.6 |
| 09cfaa16-3629-322e-bc32-a0b16f2cc5a4 | -8.8734 | -62.4495 | 2025-08-25 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| e12d40fb-c940-3b45-b74a-04c9d4cf4e09 | -8.8733 | -62.4685 | 2025-08-25 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 069e701d-6c34-36ac-9984-202db02e7f9b | -11.6023 | -46.362 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7290c892-ab2b-3b34-96d5-c8b4a7092a36 | -14.6617 | -44.078602 | 2025-08-25 00:14:00 | METOP-C | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| a18ae193-cf91-3663-becb-dd412a661075 | -13.6166 | -48.166302 | 2025-08-25 00:14:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44c542ec-f9fe-3dcc-bf5a-46b915403791 | -4.2902 | -48.257702 | 2025-08-25 00:14:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5adc5ac-8e3c-377d-9f7a-9c3ae7cfbba8 | -11.2719 | -44.974701 | 2025-08-25 00:14:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10342af2-6a31-3279-86b7-f7e6f2a49a3a | -7.5462 | -46.022598 | 2025-08-25 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab44f09-41bd-3865-b8d5-18b3307864df | -9.3179 | -40.222198 | 2025-08-25 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4df70765-b827-3bb1-ad76-020b3bc56a6d | -10.0283 | -51.0564 | 2025-08-25 00:14:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae25587a-f734-3593-aa2f-4ef39825b461 | -10.8221 | -46.383999 | 2025-08-25 00:14:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc75f00-9f3a-3506-8081-a0f58b0b816d | -11.142 | -44.796398 | 2025-08-25 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf228395-8951-327a-ae96-e111d3bb7b6b | -14.9283 | -45.548599 | 2025-08-25 00:14:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d653a35f-6f47-3dcf-be8a-773e318f1670 | -10.7136 | -47.137402 | 2025-08-25 00:14:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 363a6ed3-6476-3773-8fad-ac34d4d7450d | -20.053101 | -44.491699 | 2025-08-25 00:14:00 | METOP-C | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 017c04ef-d8ab-3798-8f03-6da83e9b93e5 | -11.6357 | -46.227402 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f4e0b38-c780-3a2f-b44b-06a2a1cdb0b7 | -7.9067 | -42.5424 | 2025-08-25 00:14:00 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
