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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7f06445-e209-3291-a4cc-7130f2a7c9c2 | -7.182 | -60.6904 | 2026-09-01 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8172fc33-e611-3102-95d5-33864793e42b | -17.3921 | -42.3495 | 2026-09-01 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 9e315af6-8473-34ba-9335-1ea627e4effd | -16.4773 | -47.9381 | 2026-09-01 02:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 6e045e58-415d-3ffa-a0a7-c7f3c8769376 | -7.3487 | -60.5883 | 2026-09-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 75db51bc-4a99-33e2-bb8c-dd8b2f455d5f | -11.2957 | -50.6008 | 2026-09-01 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 78846a6a-7b37-38b2-a341-6d7440457177 | -17.3921 | -42.3495 | 2026-09-01 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 71871751-a786-3637-b102-a726bcbab8ae | -16.0547 | -54.3908 | 2026-09-01 02:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8352de9d-db73-382d-a492-370556640077 | -18.5089 | -50.8974 | 2026-09-01 02:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 36d14a80-582b-331c-bba3-a15102dbcd69 | -10.2023 | -50.3322 | 2026-09-01 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| f0a62ecb-7736-3c78-a35c-b23a061ebe09 | -18.25 | -52.71 | 2026-09-01 02:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 39102e6f-41fc-3548-a532-519c0a413b1e | -11.258 | -50.5836 | 2026-09-01 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| fb925b96-442d-35ef-aa5d-c1aad8d28976 | -11.277 | -50.5815 | 2026-09-01 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 51cd2b2d-4729-37b9-83e4-27b9d4463236 | -6.6036 | -58.5972 | 2026-09-01 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 21e7069b-6a07-3882-91c2-445da6138f3b | -7.3488 | -60.5691 | 2026-09-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| aaca83c9-6dee-3380-8835-3a844e83986c | -10.2212 | -50.3303 | 2026-09-01 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| fdd9ade2-364c-3c26-b178-74269b51a1ad | -3.8604 | -44.0585 | 2026-09-01 02:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 42f7490c-93f7-3b40-a827-780f095a971d | -10.1837 | -50.3128 | 2026-09-01 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| cc41ed98-159f-3947-a638-cc516e0620ef | -14.4587 | -52.5151 | 2026-09-01 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| aac1a016-e097-3fa2-8477-c1ca0afb1212 | -10.2025 | -50.3109 | 2026-09-01 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 296be941-3779-3559-96d0-c14fd200c0ec | -7.182 | -60.6904 | 2026-09-01 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 641b904e-8408-39f0-b523-1836075d7a31 | -10.8627 | -45.356 | 2026-09-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9e39ca4f-3525-3984-b450-1c73117d1089 | -18.2505 | -52.6884 | 2026-09-01 02:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 51193c6e-b9f4-3422-addd-f099728cdcea | -7.3488 | -60.5691 | 2026-09-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| d9bf40fa-0c25-3041-ae90-40ac1d2ce1a4 | -10.2025 | -50.3109 | 2026-09-01 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 50b90547-5c26-35f5-ace3-2a032b958693 | -7.3487 | -60.5883 | 2026-09-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 966af8e7-b256-39c8-a4ed-e26c3855905f | -6.6035 | -58.6166 | 2026-09-01 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f70276ff-964d-35f1-9360-28c0c854a762 | -16.0547 | -54.3908 | 2026-09-01 02:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 419b9139-444d-3db4-9ed9-c8ec57df2086 | -16.4773 | -47.9381 | 2026-09-01 02:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 53c539f9-90cf-3a7f-b310-8f0edb675362 | -11.2767 | -50.6029 | 2026-09-01 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 25615086-a5c6-3de4-bb19-87f5164c6c46 | -11.277 | -50.5815 | 2026-09-01 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ef04d783-6be7-38f6-8e6b-2a5b89938e6c | -10.2023 | -50.3322 | 2026-09-01 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 6cfab0f8-06ca-33df-83c2-d0c9d8d472d2 | -17.3921 | -42.3495 | 2026-09-01 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 95ab710d-ab5d-36cc-8b96-ca84f0cf0fdd | -14.4587 | -52.5151 | 2026-09-01 02:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0df2ee24-c6d4-31f5-b800-469e3f3b5ae0 | -14.4397 | -52.4964 | 2026-09-01 02:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9509d2a8-cf0c-3622-9a79-368408e8d836 | -11.258 | -50.5836 | 2026-09-01 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| aa010bec-5505-3de9-85eb-9216e7ba6410 | -11.2957 | -50.6008 | 2026-09-01 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 038f7873-6fdb-315d-84bf-85bf33216798 | -6.6036 | -58.5972 | 2026-09-01 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a3b7681b-7d8f-37ba-b7d2-f6cc045b8e89 | -7.3487 | -60.5883 | 2026-09-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c15eb4b3-6541-3e3f-9b7d-37b6924d85d7 | -11.277 | -50.5815 | 2026-09-01 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| a2a4acfa-4bca-3661-aa02-28ef3a9649b0 | -7.571 | -60.4643 | 2026-09-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| a5e985c3-0ea3-384e-ba27-0f73f8bc7dd6 | -7.5895 | -60.4636 | 2026-09-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 77cda556-61ae-3774-926d-9d2c95dd5411 | -11.296 | -50.5794 | 2026-09-01 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 292c0040-c0b1-3bda-b23a-91e341b17504 | -10.2212 | -50.3303 | 2026-09-01 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 99b99329-c40c-362d-ad89-87a65deb497c | -16.0547 | -54.3908 | 2026-09-01 02:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3403ae24-ce13-3bc4-87a6-8ca1b48e1782 | -6.6036 | -58.5972 | 2026-09-01 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| e3a9e2f8-906a-3eb4-b995-d5d3b6df5ce5 | -11.2957 | -50.6008 | 2026-09-01 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 2f0f1439-c8d5-3e01-a70a-fee4e5a40f55 | -7.5894 | -60.4827 | 2026-09-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c2981965-ca00-39a2-89f5-7acd098d85ac | -11.258 | -50.5836 | 2026-09-01 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| ed09916a-b768-350a-adff-fde2a458c47e | -11.2767 | -50.6029 | 2026-09-01 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 59e1daa2-e706-3ec5-bd62-2f17ab1aace9 | -11.2584 | -50.5623 | 2026-09-01 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9b67e603-f470-36f0-a11f-41de9a16af36 | -14.4204 | -52.4989 | 2026-09-01 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 2a51509e-e541-30e6-ba05-5ae4f4e65bdd | -7.3488 | -60.5691 | 2026-09-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 789a9196-f677-3cd3-b945-46ddd4597f86 | -17.3921 | -42.3495 | 2026-09-01 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2a033437-2c73-3fad-b517-b1ad92c60d32 | -10.0364 | -44.6825 | 2026-09-01 02:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e21c9ca3-6a57-3db7-9062-ef4c63ada726 | -14.4011 | -52.5014 | 2026-09-01 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f303c4fc-4d5f-3299-ba17-9bd3595a8c7c | -7.5709 | -60.4835 | 2026-09-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3c83a2a4-05ed-31b3-9b57-609c69b35ef3 | -10.2023 | -50.3322 | 2026-09-01 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f45f4434-2b7a-3c76-851c-e68d41cf7536 | -10.2025 | -50.3109 | 2026-09-01 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4a4884a6-d690-37f9-9c3c-d6ac898b8136 | -17.3921 | -42.3495 | 2026-09-01 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ac374bed-59a6-3e48-a0e4-8652d92e2725 | -11.2767 | -50.6029 | 2026-09-01 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 714efcf9-4fc8-325f-ba46-46fafb34699a | -16.0547 | -54.3908 | 2026-09-01 03:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| da388c7b-533c-3697-8b28-7035dc62e88a | -11.2957 | -50.6008 | 2026-09-01 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 22c810a8-0757-3c30-b594-8c650913c738 | -10.2212 | -50.3303 | 2026-09-01 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a547e174-3610-3b9e-b895-37f71cea84f0 | -10.2023 | -50.3322 | 2026-09-01 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 5e14464a-7dc1-3250-94f8-d483fbe24a54 | -11.277 | -50.5815 | 2026-09-01 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| beb327e7-888c-3a33-8b98-ff935b282ce7 | -10.2025 | -50.3109 | 2026-09-01 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 384e0d90-8ae2-35cf-955d-6794fefd6d55 | -7.3488 | -60.5691 | 2026-09-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d79fe15d-6a8c-3007-8547-fcb10af2b56a | -11.2584 | -50.5623 | 2026-09-01 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 210e20df-20ef-30f9-97f0-ea5eb392be9d | -10.0364 | -44.6825 | 2026-09-01 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| cf3f312a-89dd-332b-bf30-0da60362c85c | -11.258 | -50.5836 | 2026-09-01 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| f5e57737-1b2b-3fce-a497-0561d980a9ed | -7.3487 | -60.5883 | 2026-09-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4cc945a2-1937-380a-9354-4d6ffc1c91b6 | -6.6036 | -58.5972 | 2026-09-01 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| bc99d2af-a42b-3713-a21f-ffca7c62dc6d | -8.84828 | -36.52572 | 2026-09-01 03:00:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 9ad74d45-8f50-369d-bec8-3aabac3a9f7a | -8.84105 | -36.5298 | 2026-09-01 03:00:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fba0da75-0eb4-3095-b300-03bac5f90f65 | -8.84734 | -36.53064 | 2026-09-01 03:00:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6b85eb8f-2ba0-302e-9a2a-2583c5f2e5a3 | -17.78907 | -39.70673 | 2026-09-01 03:02:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3262c8d6-363a-3a45-85aa-ff2e231b19b1 | -17.79546 | -39.70831 | 2026-09-01 03:02:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 91ee44f4-6a87-3737-8fa1-74325c582c9e | -21.87195 | -42.03837 | 2026-09-01 03:04:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f603a06e-043d-3c4e-8d0a-76149fbec1c3 | -7.3487 | -60.5883 | 2026-09-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7a6e8550-f498-3ac1-a759-37d58f098d9c | -17.3921 | -42.3495 | 2026-09-01 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 150552cc-d6a5-3e45-b9f0-4e761afdc899 | -6.6036 | -58.5972 | 2026-09-01 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5558f985-1a1b-3e22-ad63-86154cf9334a | -16.4768 | -47.9608 | 2026-09-01 03:10:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ac17e0a7-2e1e-3c4b-911f-31b7d34fdfd0 | -16.4773 | -47.9381 | 2026-09-01 03:10:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e19f7448-6b8d-3155-80a1-089c54783ff9 | -7.5894 | -60.4827 | 2026-09-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d1bec1f9-f87e-336d-b4d4-eb552d6f8911 | -10.3577 | -49.9957 | 2026-09-01 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 13100832-3d05-3b29-aeb7-17bd913fa56c | -14.4587 | -52.5151 | 2026-09-01 03:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a5e9495a-4988-3ea7-a432-c242d947d772 | -16.0547 | -54.3908 | 2026-09-01 03:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 46a42ccb-e920-3e16-a08d-b1e26e9fb853 | -7.571 | -60.4643 | 2026-09-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c33abb9b-256c-3832-aaf3-ed490396137a | -7.5895 | -60.4636 | 2026-09-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| e172a485-a5e2-330d-a98c-8ac9d779026c | -7.5709 | -60.4835 | 2026-09-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 4be1c5a0-b9c0-3471-88b1-c04f86223856 | -7.3488 | -60.5691 | 2026-09-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 2041aabf-1c6d-3e54-b09b-6c4b27a9b88b | -16.4768 | -47.9608 | 2026-09-01 03:20:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 06af5b34-85f7-3f00-a6e2-d54c31d48402 | -7.3488 | -60.5691 | 2026-09-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| e3ed903d-3e77-363a-90a2-719491764c38 | -16.4773 | -47.9381 | 2026-09-01 03:20:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 42c15662-8424-3983-a8b8-52c03c178b8a | -14.478 | -52.5126 | 2026-09-01 03:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b85ccc78-6860-3e2d-adab-b03e55ebaf48 | -7.3487 | -60.5883 | 2026-09-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4a0ebf4f-9c10-379a-96cc-b57333cc4abf | -17.3921 | -42.3495 | 2026-09-01 03:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7ea66614-dcaa-31e6-9f70-c3a568e5acd9 | -10.2025 | -50.3109 | 2026-09-01 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 3b7a94eb-398d-3f82-9cc2-4d46510c1848 | -7.571 | -60.4643 | 2026-09-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 33b1e70f-7076-384c-b056-f9e391e273d4 | -16.0547 | -54.3908 | 2026-09-01 03:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |


[Clique aqui para ver as próximas entradas](README18.md)
