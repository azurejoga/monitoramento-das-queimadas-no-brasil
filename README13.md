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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e618eebe-5f5b-34c9-9e9d-d3bde5c128f2 | 1.48368 | -59.92365 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8314f029-3a77-3bc6-b0bd-07693ef40107 | 3.15516 | -59.9156 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aafc853-a694-322c-9dfa-c1a786632fb9 | 3.44219 | -60.80725 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3223290-6dff-3daa-8473-e7b3b16f617f | 1.47032 | -59.93156 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| badd615d-2001-3e53-9d63-8e93c74d804e | 0.47134 | -60.39619 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 21d7dcc8-0d2e-30e7-a53f-cd974f18bbab | 1.49959 | -59.93428 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b13bba19-b55d-38a5-a44e-ef1668d61c10 | 1.50384 | -59.91982 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a9a0d8b2-34ab-326a-9ef0-4b2191438c53 | 0.19417 | -60.4429 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d13f3794-b171-3443-b4a6-e7995318f013 | 1.48477 | -59.93033 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5da8d8c-5d81-317c-8001-8ef66655b6b7 | 3.46395 | -60.8192 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 353488d8-5995-3a1a-a919-bfd88743f219 | 1.36351 | -60.30961 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c8c7a01-667c-3a4c-8442-c13255849857 | 3.15769 | -59.91768 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e5534a0-da3c-35dd-8491-fac5e657421f | 1.48582 | -59.93679 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9d23ecc-cbbe-328e-ba6f-7f1ed5045bb8 | 1.47839 | -59.93729 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3e6c9ff-868d-3f15-ba43-547a8f2f9d7d | 3.45489 | -60.80489 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d2c9c49-ef11-37c3-8126-f78f534fffb8 | 0.45579 | -60.39295 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c26323d-2bf0-3c99-8b93-ecdc2ade95db | 1.48312 | -59.92331 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| adc33a0d-62d6-32e9-87d2-85d67d5fd4ca | 3.07667 | -60.02214 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7950109e-eb74-3f5a-a3db-44a1721c9c91 | 1.4864 | -59.9117 | 2026-03-01 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 144.1 |
| df1b1084-0026-3805-96b1-d6fcce795e3f | 1.4864 | -59.9308 | 2026-03-01 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 36e78018-c5cb-3d07-9e2b-c330797bce94 | 1.5047 | -59.9116 | 2026-03-01 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 0f19ad3b-d0fb-3b26-9189-0fba82b156a4 | 1.5046 | -59.9306 | 2026-03-01 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 187be3c5-3463-3791-b893-1784ca9ced98 | 1.4864 | -59.9308 | 2026-03-01 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.6 |
| af466ca7-79eb-34af-90f3-d8364b872496 | 1.5047 | -59.9116 | 2026-03-01 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 23197884-62de-36bc-a8a9-11f63df24c64 | 1.4864 | -59.9117 | 2026-03-01 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 085f320d-ef58-3a31-b676-fd01937b9639 | 1.5046 | -59.9306 | 2026-03-01 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 4b878bd7-8807-380e-94e9-89ba3f07c510 | 1.4864 | -59.9117 | 2026-03-01 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 53584c69-b46d-3bce-8ae6-73001a9d9e47 | 1.5047 | -59.9116 | 2026-03-01 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.1 |
| c2d8fd61-584e-3919-b19c-b382279b07c7 | 1.4681 | -59.9309 | 2026-03-01 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bbe5780c-7b27-3d6a-9943-8fa85e8dbd52 | 1.4864 | -59.9308 | 2026-03-01 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 89a1427c-5a91-3e1e-8816-d52e54081990 | 1.5046 | -59.9306 | 2026-03-01 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 5ce5b625-d8f3-370b-8e5a-878f008b9cfa | 2.82177 | -60.78218 | 2026-03-01 06:54:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7044d071-6dc3-3606-95a7-a560120ced96 | 3.45375 | -60.79425 | 2026-03-01 06:54:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 53de7915-4d4a-39d9-b52c-6d18517bee5c | 1.47343 | -59.9321 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 77986b01-b19f-33bb-9cc5-a12630717cd9 | 1.49342 | -59.91449 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.5 |
| feb21679-5126-3560-b3f0-9de8266ecebb | 1.47128 | -59.9177 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e1e28387-f907-3432-b52a-46a1b7b2a5f9 | 1.50227 | -59.89825 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 76224dba-55d6-37dc-9feb-3cc37075e68d | 3.16335 | -59.91134 | 2026-03-01 06:54:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 23.0 |
| c814c167-e29d-3486-bc16-63ceb3cfe6c3 | 1.48449 | -59.93031 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 5926345d-0c60-3cbc-afa1-e1dba2fdc10e | 1.08491 | -59.2501 | 2026-03-01 06:54:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 16878173-fac4-3d2a-8312-2b7ccd178ebc | 1.51547 | -59.91064 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| e62a9e2b-aeae-3114-8453-36cadf315bcb | 3.16241 | -59.90575 | 2026-03-01 06:54:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 858b8e1a-9502-3f28-975a-2e5ea4d08614 | 2.81914 | -60.76448 | 2026-03-01 06:54:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 68f0cffc-0414-3b58-ba25-00ccba0c2e7e | 1.49559 | -59.92881 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 051d5469-563d-3546-a813-4eed4bc9f8e4 | 1.06403 | -59.25319 | 2026-03-01 06:54:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a2a30783-021e-3abc-aa35-2d368deca3a8 | 2.82461 | -60.77447 | 2026-03-01 06:54:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 291fb274-b80c-38f6-8da0-042b100f8caf | 1.51776 | -59.92561 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 9ede51dd-b25e-35d5-a48f-d181c082fb29 | 0.19134 | -60.44028 | 2026-03-01 06:54:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 64bf9e3b-549f-3d8d-a06e-790d24e62dbd | 3.16458 | -59.9211 | 2026-03-01 06:54:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 792b1561-3c38-36ac-b36c-dc2bf2d157cc | 1.4912 | -59.89975 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 8d1ba12d-0338-397d-812b-25bd65cb6af3 | 1.48235 | -59.9161 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| cd5b1fed-1819-396c-8196-5b5d18c23dd2 | 1.50666 | -59.92712 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c31aa705-f891-31dd-8e96-6c5ef58f6596 | 1.50818 | -59.92116 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 625d0950-3469-3abb-b49d-3c6b00c625e4 | 1.50607 | -59.90658 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f7859275-d46b-3cdd-a6b4-09ed55ac9133 | 1.51923 | -59.91933 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 112c7f1e-5f40-337f-a663-c4ef35215663 | 1.50447 | -59.9127 | 2026-03-01 06:54:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 8c94380a-6563-39c3-8512-e6c92241e3b6 | 0.47145 | -60.38958 | 2026-03-01 06:54:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 043c368c-0a72-32e5-b58c-68331212b2c4 | 3.45642 | -60.81255 | 2026-03-01 06:54:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6069d52b-1d5b-33c8-bfa8-5f37c0293828 | -18.80853 | -57.62998 | 2026-03-01 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 1b920a01-bd77-399e-b416-a6274c8e11a5 | 1.4681 | -59.9309 | 2026-03-01 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 101a2065-5b3d-3d11-b72c-24a88f207799 | 1.4864 | -59.9308 | 2026-03-01 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 07db4d32-ee28-3714-9107-c9c9b9372c58 | 1.4864 | -59.9117 | 2026-03-01 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 154.7 |
| e0208e6b-6e2c-334f-b8ca-24b8ab844156 | 1.5046 | -59.9306 | 2026-03-01 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 1c8f8bf8-bee6-3f5e-9ddc-8f42bf5daad3 | 1.5047 | -59.9116 | 2026-03-01 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 7be1eae3-dd04-3abd-9a45-0965c9a87da9 | -21.70776 | -56.31909 | 2026-03-01 07:01:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f49814ce-3119-3f28-b481-2d9078924a7c | -21.70947 | -56.30568 | 2026-03-01 07:01:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dbe02827-8b29-37e6-8a70-3f3b8cd87ac8 | 1.4864 | -59.9308 | 2026-03-01 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.0 |
| c360879e-72a3-3a39-addb-4ed86c9ba66d | 1.4864 | -59.9117 | 2026-03-01 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 60c5e3d1-6822-323e-b014-a3a42c6a38da | 1.5047 | -59.9116 | 2026-03-01 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 92172f51-ab57-3ddb-b97f-6019d36edf88 | 1.4681 | -59.9309 | 2026-03-01 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a14d81d5-2cba-3ad9-9d62-5e68211b68a3 | 1.5046 | -59.9306 | 2026-03-01 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| db2fa35a-27ce-36f6-bbe1-be1634bcad9d | 1.5046 | -59.9306 | 2026-03-01 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c47d08bd-5548-36f0-b554-7642e0a0e412 | 1.5047 | -59.9116 | 2026-03-01 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 90bfe17a-7b63-37b2-9535-e550005e10a7 | 1.4864 | -59.9117 | 2026-03-01 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.4 |
| d39c6fb7-4d20-3554-b868-be1abf75ab3f | 3.0548 | -60.6901 | 2026-03-01 12:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 41c9492b-ff8a-3a14-a5ab-7d92a7f7c3ba | 1.4864 | -59.9308 | 2026-03-01 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f5934566-3ae7-342c-a8ae-cbbc759ca6d9 | 1.5047 | -59.9116 | 2026-03-01 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 7c8c278f-418e-3524-ad3f-4dd1dce71010 | 1.4864 | -59.9308 | 2026-03-01 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 48f44d7d-434b-36d6-99b3-e5b3b3c8adf9 | 1.5046 | -59.9306 | 2026-03-01 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8d3145a2-851f-33bb-8935-721e9bb5212d | 1.4864 | -59.9117 | 2026-03-01 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 1e69690c-fd24-3b97-8b2e-8fbb7c88bbfd | 3.0548 | -60.6901 | 2026-03-01 12:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5c4d05b8-b72f-3b0d-9638-e080f8ecdd22 | 1.5047 | -59.9116 | 2026-03-01 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 203b29b2-59ac-3474-aa16-541d09721cea | 3.4381 | -60.8161 | 2026-03-01 12:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7d0551e3-dd47-34ba-b7d5-5aa3279d42a1 | 1.4864 | -59.9308 | 2026-03-01 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 19b3def3-73bf-3c46-b0be-904a75b95d57 | 1.4864 | -59.9117 | 2026-03-01 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 142.0 |
| f622c258-abad-3a35-b016-6e170b49ab60 | 1.5046 | -59.9306 | 2026-03-01 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f6d5483c-c1d7-33eb-948d-ca0024d9ec1b | 1.4864 | -59.9308 | 2026-03-01 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 70f2da69-f2f4-3130-a98c-88d2b6d7995f | 1.5047 | -59.9116 | 2026-03-01 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.8 |
| c4ecd4eb-ddb2-3e9e-bf3a-201210a2698d | 1.5046 | -59.9306 | 2026-03-01 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0f6f60e4-9c93-37d9-afae-21feff58013c | 1.4864 | -59.9117 | 2026-03-01 12:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 1e3230c5-b9ea-3bd6-82c4-bc672da2ad86 | -18.80481 | -57.62616 | 2026-03-01 12:31:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| fd8b5206-87be-3147-8fbb-c327c86cdb4e | -18.81252 | -57.63354 | 2026-03-01 12:31:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| b7a29bb5-c1cd-3dab-97e7-238eaeccb6f4 | -19.25846 | -52.90086 | 2026-03-01 12:31:00 | TERRA_M-T | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 41631f2c-4216-33a6-86b6-d9fecbf3be13 | -18.80333 | -57.636 | 2026-03-01 12:31:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| e269c05b-beec-3263-bdc4-01f4984725c8 | -21.48406 | -51.52833 | 2026-03-01 12:33:00 | TERRA_M-T | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 3c9a6be1-c9e2-3681-9362-33e6579cf76c | -23.94043 | -53.51427 | 2026-03-01 12:33:00 | TERRA_M-T | CAFEZAL DO SUL | PARANÁ | Brasil | 4103479 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 85f3aa27-f667-318a-b6aa-ce57f9d35f38 | -23.73277 | -53.21478 | 2026-03-01 12:33:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 5de91a33-dffa-3388-8511-4d364ea233d3 | -23.72888 | -51.64082 | 2026-03-01 12:33:00 | TERRA_M-T | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| fd93261d-13fd-3acd-9719-94015739688a | -23.96688 | -53.71756 | 2026-03-01 12:33:00 | TERRA_M-T | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 25064093-4121-3df4-abe8-ce0b097ab63b | -23.28867 | -55.33136 | 2026-03-01 12:33:00 | TERRA_M-T | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |


[Clique aqui para ver as próximas entradas](README14.md)
