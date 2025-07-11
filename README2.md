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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10654de9-3656-321f-9b85-04b1127af465 | -7.2001 | -43.133301 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d69f1012-c51e-3250-a979-62bacdf8d36e | -10.6282 | -45.227798 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db5ccee1-434c-3c72-b6ff-f1c3de0a7bb3 | -8.3625 | -51.082199 | 2025-07-11 00:41:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54e25fe4-e6f4-3298-853b-63de9504cb8a | -6.0928 | -44.873299 | 2025-07-11 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b03ced69-3b80-3947-b7ba-5f0efcf09d09 | -11.8538 | -46.7514 | 2025-07-11 00:41:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca3eab52-2a91-3ef7-a81f-6588475600df | -4.5485 | -48.006802 | 2025-07-11 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3460aa93-8f32-352e-81bb-6a8e5da9f5d0 | -11.8409 | -47.5023 | 2025-07-11 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0e8b8a0-6d30-3fd2-b8c2-ee5d353678d3 | -6.0904 | -44.863499 | 2025-07-11 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d371ce4f-9f0c-35e2-9db7-7785588dbdcb | -9.5396 | -46.304001 | 2025-07-11 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03567a36-a70c-3835-aaeb-b14f4358cecc | -8.3821 | -51.077801 | 2025-07-11 00:41:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb29984d-d391-3b50-90b2-44f691b03c45 | -4.2291 | -47.209599 | 2025-07-11 00:41:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 559db3a1-3544-368a-8f87-ab15c6d8f1c1 | -10.8575 | -49.120701 | 2025-07-11 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96e19113-044b-38da-8d93-75d2d945f14d | -7.197 | -43.374901 | 2025-07-11 00:41:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40c882bd-926d-37df-adc9-2ef629b9138a | -9.9181 | -47.844501 | 2025-07-11 00:41:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a27cc6e-f624-38fb-8ff8-70f9d3f2e8a0 | -7.1942 | -43.108898 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70850863-8de4-3f8a-9571-d217a5147cbc | -12.0746 | -47.9846 | 2025-07-11 00:41:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63550d38-3f32-34c5-9b69-bbe5311c3e6e | -7.4997 | -43.9426 | 2025-07-11 00:41:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1275e8e3-9b7b-358e-93ad-a062e7653410 | -10.6738 | -49.495899 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38235f0b-11ee-33c5-94e9-b991b2fdb6ff | -13.3726 | -47.8904 | 2025-07-11 00:41:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c9b05fa-d4f5-3f98-b6c8-6ebeebbd08f8 | -12.5574 | -52.213501 | 2025-07-11 00:41:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2060a751-b89d-338b-be36-81f6e545a236 | -7.2069 | -43.118801 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8c2abb51-042f-32ed-a6d7-06332425bf00 | -7.9501 | -49.658501 | 2025-07-11 00:41:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 611c3873-4842-389a-9f11-50458a6011d6 | -8.3804 | -51.070202 | 2025-07-11 00:41:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a12c77e8-d9d2-34ba-a689-ce3d123e82ba | -10.5818 | -49.1315 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7be58c86-a73a-3cc6-81ee-df8686bcd4fe | -12.6657 | -47.094501 | 2025-07-11 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12f9350d-f647-3f56-8dcd-683431352cd3 | -6.8812 | -45.237598 | 2025-07-11 00:41:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76eec74f-6acf-32c7-af6a-6e00daec15cd | -5.9219 | -45.587299 | 2025-07-11 00:41:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b58e1d40-3331-3e1f-ba48-91867c987279 | -10.682 | -49.486599 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca68a839-1436-3881-9983-666b60b94760 | -2.9221 | -48.244999 | 2025-07-11 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb1b8d8f-d430-31d0-a458-cf31e31cd975 | -11.338 | -45.214001 | 2025-07-11 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da3b8a1d-b03d-3a82-a068-ce5332e08643 | -12.9932 | -44.871899 | 2025-07-11 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56543692-f8dd-30a5-92c9-8c714bf6d991 | -4.7934 | -45.351601 | 2025-07-11 00:41:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d71aa923-a24e-31ea-bb20-bb0d4262cb3b | -9.8641 | -47.879002 | 2025-07-11 00:41:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8218f744-35c1-332a-b072-ba288dbc959a | -6.8791 | -45.2285 | 2025-07-11 00:41:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a54f3fb1-df4c-3729-b728-72294d2d1e7b | -5.5612 | -43.901699 | 2025-07-11 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 555fc813-4277-3efa-8515-16c5ac5cf5d2 | -9.5378 | -46.296299 | 2025-07-11 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45c80004-3fd5-39ef-88d2-339d2bf9de7e | -5.7999 | -45.116501 | 2025-07-11 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32d45c6a-4d76-393c-ba4b-bd4652966dd4 | -6.083 | -44.875599 | 2025-07-11 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df996650-d234-3c85-bbdc-e719be759864 | -9.9149 | -47.830601 | 2025-07-11 00:41:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62f5956e-aa56-32fb-87dd-a0b90f1894a1 | -4.2309 | -47.2174 | 2025-07-11 00:41:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3103ebe4-73af-35d5-9e0d-9f0f53306df6 | -11.9392 | -49.308498 | 2025-07-11 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bae6a845-02f2-39b1-ad18-bb40cc502490 | -6.6806 | -46.3092 | 2025-07-11 00:41:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9981e8-d58f-3424-a4b6-c7d34d7a9dbd | -9.6207 | -49.027 | 2025-07-11 00:41:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef46c640-4acc-3726-999e-7596d28e93f9 | -10.6706 | -49.481701 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f05bbb8-ea2c-3d96-8eeb-c627cbbdf28a | -6.1632 | -47.272999 | 2025-07-11 00:41:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16cc75c3-70ed-381f-90d1-29bd3e152e9f | -12.4072 | -45.364201 | 2025-07-11 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95d12d9b-0be0-3a13-9b34-b38206071556 | -11.4493 | -45.117298 | 2025-07-11 00:41:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05d29c09-6786-3f34-96d8-37b66731dccd | -9.536 | -46.2887 | 2025-07-11 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 111c7f97-2244-31e8-a4ab-5cf532f11d9f | -6.8618 | -42.8027 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0c1c1968-5eb8-3d0a-8af3-055d80189052 | -7.0828 | -49.606602 | 2025-07-11 00:41:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d601d7ab-f6ba-36d0-81a2-208eaa6759c7 | -13.3644 | -47.899601 | 2025-07-11 00:41:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da2f25f9-c552-3fa7-a470-38ff6aff3586 | -7.9516 | -49.665501 | 2025-07-11 00:41:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a87c34e-e51d-30ff-a5c7-41a86d09a4dc | -7.9567 | -44.855801 | 2025-07-11 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74cb0ad7-a1b7-3b1a-a8f4-9a3b0e707847 | -7.5624 | -45.627998 | 2025-07-11 00:41:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65173b8f-5f48-3abc-96fe-e00ccaa1dbd4 | -7.2167 | -43.116402 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a729a0a-7a78-3712-8ae2-387c856e6482 | -7.1972 | -43.121101 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d7d4fd2-0f24-3b90-9bfb-ba3381602eef | -9.6615 | -49.894798 | 2025-07-11 00:41:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95dab902-f229-3b33-9964-f2cd5de74e90 | -12.0197 | -49.532799 | 2025-07-11 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a706467e-9886-3a29-976f-d9009b0078ce | -14.3962 | -43.778702 | 2025-07-11 00:41:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce8e5425-ebc7-36f2-99e1-9e614b8ac5cd | -13.3628 | -47.892601 | 2025-07-11 00:41:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e28641be-f67e-3574-bb0e-d78c9995fda7 | -10.5767 | -49.1548 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45babdba-6690-3fca-9976-02641b57d696 | -10.5735 | -49.1408 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a6e8432-b353-3135-b33a-3f006ce8d9d9 | -10.5802 | -49.1245 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 648e4ae9-cf56-3d6a-94b1-50aecdcf3269 | -9.2012 | -45.266499 | 2025-07-11 00:41:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 197a8ab0-b462-3a27-9e9d-07e1e904ac1f | -9.6599 | -49.8876 | 2025-07-11 00:41:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 623c793a-b499-38a0-99df-9bb387852c2a | -12.0571 | -48.5462 | 2025-07-11 00:41:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cd2d1b3-133a-34de-9303-df80b71b826e | -10.6754 | -49.502998 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cda7922-b35a-3934-9617-afaa8674a231 | -6.165 | -47.280499 | 2025-07-11 00:41:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18a38976-31a7-3b46-babc-0bd19c8fa885 | -12.4169 | -45.3619 | 2025-07-11 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97e9bef0-fba1-31f7-ac50-c82641903b2f | -14.4059 | -43.776199 | 2025-07-11 00:41:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6192ca1-748d-38a7-b9c3-db9f2506079a | -14.394 | -43.769699 | 2025-07-11 00:41:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce60f610-4a53-3840-9467-36f88ed99b49 | -13.001 | -44.861301 | 2025-07-11 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09efc524-8978-336f-9c2d-7c9dcd85557f | -6.7381 | -44.3367 | 2025-07-11 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1311809-1029-382d-ad4a-c457ea2ab10b | -9.6191 | -49.0201 | 2025-07-11 00:41:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be83b2c4-690d-3282-85a8-f3ac10d82d61 | -6.6787 | -46.301102 | 2025-07-11 00:41:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7118dbb2-33e5-31fb-862a-af1978908826 | -5.9198 | -45.5783 | 2025-07-11 00:41:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 240100d8-68f3-3d89-b06e-eba5416b3aba | -11.8555 | -46.758598 | 2025-07-11 00:41:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 506e3426-ecdd-3ee1-a967-15cd912c68de | -14.4037 | -43.7672 | 2025-07-11 00:41:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49d8100e-e03a-3f9e-97d6-ea78d4e4c047 | -6.9066 | -44.0509 | 2025-07-11 00:41:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a85c172-cee6-3873-b0a2-d00c35bd2365 | -12.0342 | -48.765202 | 2025-07-11 00:41:00 | METOP-C | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e4c09b3-31aa-37ba-8cc7-cc1e0cbde374 | -10.5751 | -49.1478 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb0db60e-7af0-3d8f-ab47-650c974aba17 | -5.5488 | -43.892502 | 2025-07-11 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc6f3d62-ac11-37d3-b5c7-bcf05740e461 | -6.9092 | -44.0616 | 2025-07-11 00:41:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 387399de-4e6b-347b-b375-0389f26a013e | -12.6673 | -47.101601 | 2025-07-11 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e083552-aff0-38e1-b7a4-ef0b73b99b6c | -9.7928 | -47.748199 | 2025-07-11 00:41:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3869032c-d432-38d6-ba4a-1e55bb2516f9 | -7.4971 | -43.9319 | 2025-07-11 00:41:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 257545fd-071c-3d28-924a-f88425c98fe2 | -8.6755 | -49.951302 | 2025-07-11 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589b8daa-0fac-393a-a54c-7e729545a804 | -10.6722 | -49.4888 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1852769c-d0d8-3255-8455-5b1e928a35ff | -10.5833 | -49.138599 | 2025-07-11 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99ab6a2e-ffba-3c6d-bd29-cdafdb64c428 | -11.3271 | -51.439701 | 2025-07-11 00:41:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbcb0511-40a2-3334-9808-fa1076935704 | -6.0807 | -44.865799 | 2025-07-11 00:41:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fac40187-fec6-36d0-82c1-fe13787190af | -5.8438 | -48.387001 | 2025-07-11 00:41:00 | METOP-C | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 741945a7-b1ea-345e-a52a-4e8a24f591c0 | -10.8477 | -49.122898 | 2025-07-11 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e56d0d9a-fa61-3486-a0d7-aca599fa6f24 | -7.1942 | -43.363098 | 2025-07-11 00:41:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac9207cb-cf50-385a-b921-c6addaaa0708 | -4.5502 | -48.014 | 2025-07-11 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2fdd89-996c-3658-8cff-b3f186e26a95 | -8.3838 | -51.0853 | 2025-07-11 00:41:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a518b8a9-adb5-3078-9cea-ff66486d2d76 | -5.5543 | -43.915501 | 2025-07-11 00:41:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 424d52c1-3f56-33a1-a0b2-b0bb449f73a7 | -10.8461 | -49.115898 | 2025-07-11 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd98b3dc-bd1b-3593-9c3e-8676c6b7d050 | -12.5594 | -52.223099 | 2025-07-11 00:41:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2b8f89e-a584-308d-bd49-c8eb3652c08f | -7.204 | -43.106602 | 2025-07-11 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
