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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79d3496c-9011-3c47-87c9-df28d16028f3 | -8.086 | -57.68151 | 2024-10-03 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85822299-52ba-33a1-968d-c637f486270c | -11.98852 | -57.19228 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39261932-2317-35c5-8639-142222197899 | -11.98791 | -57.19639 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4eab59cd-7f9f-3175-9b1a-9a22b22386c7 | -11.98769 | -57.19115 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ed88244-43eb-3293-a473-629b49c081ef | -11.9871 | -57.19527 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 24a0bb48-b345-3e15-ab1f-e9f6b412a8d4 | -11.98495 | -57.19173 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dde7cbf4-f42b-3d08-acd8-9e0d4efb18ca | -6.86731 | -59.03315 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45cafc1b-be4f-38cc-92c0-03122c99ed9e | -6.83416 | -58.98544 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5db25f2f-a320-3072-a6ce-11e93597ae0a | -6.97957 | -59.09727 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1271db42-5525-34f7-8a2d-640c8e3944aa | -6.97572 | -59.10021 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54ecf7d3-fcfa-39a9-86b4-51107d258d20 | -6.97296 | -59.09624 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7817e51-fbbf-31c1-b435-fdfed028253a | -6.97242 | -59.09969 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1bfe33c-5913-3d46-90d7-894e4096085b | -6.96966 | -59.09571 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 105d4e81-16ca-3c05-8a4a-a2e721841345 | -6.88112 | -59.05304 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc015930-7559-392b-971f-be3f9c6a4e72 | -6.88058 | -59.0565 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70eef059-5755-3826-a438-9b1152b43816 | -6.87999 | -59.03869 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6868b166-b986-3519-b2e3-d1d2a99436d5 | -6.8798 | -58.95365 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8f19a9d-552f-3b7c-9758-8b37c900bde7 | -6.87945 | -59.04215 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f7111f4-1db9-35d6-9653-bc99985ea523 | -6.8789 | -59.0456 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27e0b87c-fd58-396b-9ee9-65a1b0db2c8f | -6.87836 | -59.04906 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89368ff5-2da5-3583-ad76-b81bb7bb412b | -6.87782 | -59.05252 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87de3d1-2948-34b9-950a-20270879b0c0 | -6.87727 | -59.05597 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a775ac8-85f6-3375-9df4-f40d814ac89d | -6.87723 | -59.03471 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83b35ca6-ef4b-3362-8aee-c806be40ff67 | -6.87668 | -59.03817 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af76d7d0-b445-3101-8744-7207a1997a08 | -6.87614 | -59.04163 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 232abb3c-5886-3aaf-81da-9c05d4618696 | -6.8756 | -59.04509 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70fc7169-b779-38fb-b003-fa9d465a1b42 | -6.87505 | -59.04854 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75498cc6-32de-3bd6-a51d-963ea7ef9d6f | -6.87451 | -59.052 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 540a4378-09de-3a02-bf04-584a19c8e5f7 | -6.87446 | -59.03074 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c74bd467-c8c8-3176-b997-b8bc2208b315 | -6.87397 | -59.05545 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aedd570-7684-3498-ad48-c743625c44bf | -6.87392 | -59.03419 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4f0e55b-2952-3df0-a999-d3e1a0307f0a | -6.87338 | -59.03765 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9982dc4b-9e9a-3ec4-abb5-d67889aee8e2 | -6.87283 | -59.0411 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 384fc9a1-cd86-3807-a8a7-c75e4e86eaae | -6.87229 | -59.04457 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55071ea0-57ad-3213-a088-1e89de3749a0 | -6.87175 | -59.04802 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2345add6-0831-3975-8904-6008e90495e2 | -6.8712 | -59.05148 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7c601a1-2c9d-3a11-898f-bd4d4579eb3e | -6.87116 | -59.03022 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e24921-03b5-3380-85b2-bc4ca18175f5 | -6.87066 | -59.05494 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bf16ac8-4cd6-3576-b157-345466e85207 | -6.87062 | -59.03367 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b416edb2-0d53-30ef-a995-716b56ca43c9 | -6.87007 | -59.03713 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4416a241-73d2-3811-b2b3-eee78e163571 | -9.19394 | -58.19824 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb9ce2f2-2006-381b-a198-6a40bd9d5fe0 | -9.19339 | -58.20183 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d6f2d43-43a6-3c01-9fb0-1d0adf702a98 | -9.19279 | -58.18331 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba7ef73-fa7a-383a-89f5-0b0e0d5ad555 | -9.19168 | -58.19051 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12cc30f5-e344-3705-b5b5-cec10aebc845 | -9.19003 | -58.20131 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0f6fc81-7a9d-363d-9ca6-80669c2b7938 | -9.18888 | -58.18639 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b275dd4f-e659-3cc7-9706-fece4d50ecb8 | -9.18833 | -58.18999 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56d9f422-4c55-3973-b837-46737dc49c95 | -9.16884 | -59.36658 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e98de706-44e9-31f9-91f0-e4a053611437 | -9.16829 | -59.37006 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c751963-e377-3e3f-b7b4-c0d49ff3c3de | -9.16721 | -59.37702 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a108382-1338-302d-aafb-c75fc15d43a0 | -9.16666 | -59.3805 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 292a8544-5b38-36d9-aa3e-814d95bc3619 | -9.16553 | -59.36606 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ea1c8c6-da3e-33dc-a8e4-d03e7afbc3a4 | -9.16499 | -59.36953 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d310b36e-f77e-34f5-9c74-57ac72b218a2 | -9.1639 | -59.3765 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a20ba5b2-ccd7-3b91-be01-e297b361cd1a | -9.16335 | -59.37998 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36a2c377-d3af-392c-8598-e2873a07b379 | -9.02524 | -58.89346 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a06c254f-939e-3d26-ab27-98770099ab0b | -9.01217 | -58.91301 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c1d8367-6ddb-341c-8b95-6b760c2ef398 | -9.0094 | -58.90898 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cf7f184-3087-3fdf-87a4-2828e2316909 | -9.00832 | -58.91597 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ec8592-8499-3631-915b-6231b7efcd7b | -8.09347 | -58.04754 | 2024-10-03 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6230e319-5720-3936-b6e5-0afbc00d5669 | -9.19224 | -58.18691 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd90cc2-7ae2-3f28-a277-114e44a0d746 | -9.18943 | -58.18278 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c1fe0e7-877d-37e3-b9a0-f974ad885183 | -9.16775 | -59.37354 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c8fcbbf-6b34-32a9-b952-0b53c4d7cf54 | -9.16612 | -59.38398 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb7c4709-0047-3702-ba00-6d19f194a088 | -9.16444 | -59.37302 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4de42093-df11-35a0-b2b7-31fabe80b3f0 | -9.16103 | -59.37244 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91bd261e-0d93-3988-a23d-fc495882d254 | -9.16048 | -59.37592 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17762b45-d5d5-352b-8c1c-e9ab018e1694 | -9.0247 | -58.89696 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47935834-23ca-347c-abac-5f8ead966831 | -9.02193 | -58.89294 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f62d434-8047-36c0-bc09-cbcc05428163 | -9.02139 | -58.89644 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c79b660a-ddf2-3cd1-9ca7-a7ab4423a58e | -9.00886 | -58.91248 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72774ad2-ec92-3f24-87fd-f193ac556d9d | -9.54325 | -59.42616 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4975659-631f-35a0-8664-b8af27ace16d | -9.4677 | -58.97386 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e076422-48bc-359f-a0d5-061885d0c1ec | -10.72528 | -58.51836 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 152fb46c-c2c5-3b9c-bb6c-b220d9331d73 | -10.72192 | -58.51783 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f9ba0a3-cd9f-3821-9f25-176665436449 | -10.72137 | -58.52145 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b90a472f-09b6-3e04-8bdc-4da4580d4bbc | -10.72082 | -58.52506 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c411936-8927-3a2e-a22d-45eb7158b9e8 | -10.71746 | -58.52454 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62493f71-fec1-345d-b290-f723357517c2 | -10.71691 | -58.52815 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b831159-56fa-30e1-a5ee-6f08eb8c43fe | -10.71355 | -58.52763 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c18dfa1c-cb08-3dbf-879d-6f2382795a4a | -10.70354 | -58.54828 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43f37a8b-129c-3de1-bd51-b73040aff7ff | -10.70299 | -58.55189 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97e7d7f5-9a1f-3b9c-8a11-8de497c9ba72 | -10.70244 | -58.5555 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6d9bddd-b60b-3115-a7a2-720de1217ddf | -10.7019 | -58.5591 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d46f903f-09c0-3655-a34c-e33d07df8008 | -10.70135 | -58.56271 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cd303ec-ae4f-3f74-9124-aa53dda056c1 | -10.70101 | -58.55159 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9ddd614-9dbe-37cf-b473-65dbba9d08f8 | -10.7008 | -58.56632 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2caf6b13-7b40-3db9-b431-4de52ebb6148 | -10.70045 | -58.55519 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f047daa-1691-365b-9cd2-fd9ec10fb376 | -10.70026 | -58.56992 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea4aa3d2-f06a-3ed5-8f14-fbde552a2246 | -10.6999 | -58.55879 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e84e019a-ed38-3fec-b267-c20b91c0b6aa | -10.69934 | -58.56238 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d8eb1ea-4269-3d0d-a1a0-abcd19663dd2 | -10.69879 | -58.56599 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6926092-8254-3b2e-ab49-ea914b80a675 | -10.69823 | -58.56958 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35620790-4f7d-3cec-a09b-13336e8239af | -10.69807 | -58.58435 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6940b02f-0571-37bd-9668-41b9657ce626 | -10.69596 | -58.53968 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2dbbfc2-bf2c-3b7e-a634-33f670db6c8b | -10.6954 | -58.54331 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5625f138-beb5-3eac-9466-27ec16a13758 | -10.69261 | -58.53915 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5558f4ed-5cdf-3f0d-93fe-eb48673f9c0b | -10.69204 | -58.54279 | 2024-10-03 05:16:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5f9199-2ec8-34d3-9c99-ea38c1ee37a5 | -9.96697 | -59.60424 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6da35cf5-2189-31b3-919d-63387289b848 | -9.82969 | -59.41832 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README164.md)
