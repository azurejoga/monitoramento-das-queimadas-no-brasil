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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c1ac6b-6ee7-386c-8db9-6de9bcded2ea | -10.49063 | -36.83575 | 2024-12-17 04:33:00 | AQUA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 054395ca-528b-3369-832f-5a8cddf64307 | -10.47883 | -36.84549 | 2024-12-17 04:33:00 | AQUA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| db8b6155-4967-3346-a4d3-884bdb2ef0d1 | -10.48875 | -36.84732 | 2024-12-17 04:33:00 | AQUA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 40.5 |
| 00c03aff-1c2f-38c3-9aec-2ecbb2ea01b9 | -15.0865 | -59.6487 | 2024-12-17 04:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 20ca4b6f-7e19-38cf-8762-70d8339a58a6 | 4.4435 | -60.9846 | 2024-12-17 04:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 23445217-9400-35ff-bc87-0382e1250c3d | -6.9346 | -43.5168 | 2024-12-17 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2bf3c239-2f20-34cb-b099-117edc7898d8 | -5.0936 | -43.9176 | 2024-12-17 04:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 746fe37c-0fba-3578-b705-abd25bf6fdf9 | -5.0938 | -43.8945 | 2024-12-17 04:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4cdc84cd-3848-3e98-9aa3-a623395d3600 | -6.9349 | -43.4934 | 2024-12-17 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4f093382-e185-37b6-b552-94096f99273b | 4.44298 | -60.96223 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1e54a5fd-1146-33c1-9459-54c8c4a536ea | 4.44527 | -60.97839 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04a09181-5c1f-377b-9a6b-7736c928add5 | 4.43644 | -60.96344 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46e5f957-8a34-3cbe-93b7-a5524def2f44 | 4.43872 | -60.97961 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b2c4f57-0ef4-3b50-b00f-56da1625c44d | 4.44671 | -60.98861 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 772bc3e1-7671-3bb7-ac2f-143837d55048 | 4.45939 | -60.98312 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de69da36-3e83-3069-8058-4489c6fbc6fb | 4.45249 | -60.98188 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f3917363-fc60-3e56-b64d-b01d6c307d64 | 4.45175 | -60.97663 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0451e615-7264-3d86-8593-290cb37e0db2 | 4.44599 | -60.98349 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2d2c33ae-fc50-34b7-938f-73528f1bdf41 | 4.43944 | -60.98475 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f38f00ec-10da-35cd-b881-982cfa36acbb | 4.44224 | -60.95698 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22d171d2-5194-37f7-affe-7f618ece417b | 4.45101 | -60.97147 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6a01cde-0d22-31d5-993c-6335ee414b2f | 4.4402 | -60.99013 | 2024-12-17 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 38da39a9-f872-395b-92a2-e11c2bb02ff3 | -4.02578 | -47.03519 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09c4ccdf-d258-337d-a9a4-036ad2307399 | -3.99381 | -44.17393 | 2024-12-17 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e865667e-1a61-3c3b-b42a-701ce5b1e005 | -2.60587 | -48.25941 | 2024-12-17 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aba9736-feeb-3a0f-965c-9cf34e6a9116 | -3.7935 | -46.84212 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23da22d7-871c-3876-800e-faf94b9957d5 | -3.76358 | -47.16601 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da41e232-c880-3213-aef9-1d6454e013e7 | -4.39769 | -41.43139 | 2024-12-17 04:44:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 28ffac2a-887c-375f-9062-1baa5c29e4f7 | -3.79722 | -46.84275 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97df5515-e8ac-37f4-a412-32474fd858a9 | -4.03887 | -47.02384 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9fbf53d-ccae-3e5d-b908-a0209ddf79f0 | -4.30067 | -43.8927 | 2024-12-17 04:44:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b88c0610-2efc-3080-84d9-713d2f7e25eb | -4.68013 | -44.04269 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9320ceb-a63f-3c52-a1ee-d60b9027ccc1 | -4.06476 | -47.46152 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a50574a6-21ec-3b31-acd8-4726ca6cf552 | -3.95913 | -47.03538 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 676c04d3-ea2e-35c1-beba-23fc621d902c | -3.30368 | -53.36581 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8810bce-0321-3e0c-a019-4f8483d01856 | -5.11857 | -43.20092 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e47702d-71a3-3aa3-9050-b0a44c90e896 | -4.05634 | -46.90971 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38651bde-8a74-3ece-a86f-5c4b8572e4af | -2.0546 | -46.65639 | 2024-12-17 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c8c2c2d-27bb-35b3-830c-ea06ebb0efef | -0.75469 | -47.75701 | 2024-12-17 04:44:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6d1d574d-cd57-3b22-9090-86853ec2b7b6 | -4.65184 | -44.32849 | 2024-12-17 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 601b916a-5c7d-37fb-90ba-da6fe5b4dc6d | -4.5698 | -46.57835 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 206a6a50-6793-3be5-ac87-1f6644886d3b | -4.39959 | -41.43444 | 2024-12-17 04:44:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 961ce73a-f09b-3102-b90a-da5d0d8f1aac | -1.39822 | -52.68742 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9aeb3521-3865-3959-a51b-6b5ce98b42df | -5.9633 | -41.59594 | 2024-12-17 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 027a55d7-62a5-3a83-8ecc-0678f2c3cc66 | -1.46472 | -46.80824 | 2024-12-17 04:44:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 900f1a52-b28e-3e89-b303-10d52ec59cff | -4.09874 | -46.73307 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3031cfda-19ff-31f6-8734-63fd2d0b1a23 | -4.05261 | -46.90913 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de0e2750-6744-3016-a43e-5c70b18b3640 | -3.04247 | -47.94843 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec41a4b1-b7ae-3aac-b3dc-32b15474376a | -3.96095 | -47.97392 | 2024-12-17 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa0dfe55-0f2d-3ae2-800a-846b7830b960 | -4.96598 | -44.96309 | 2024-12-17 04:44:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d72cabd3-5062-3fc3-8191-def41ea01614 | -5.2075 | -43.29539 | 2024-12-17 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d0cb295-2a5b-394c-829c-512d4b74f9b1 | -2.49072 | -49.04829 | 2024-12-17 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50de8cfc-5121-37f5-b31a-22b05c6c058d | -4.02949 | -47.03572 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f969ef6-2c90-3ea3-b125-6d0c6692c351 | -3.99517 | -47.28462 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efc9911e-4455-3db2-b4e7-03263aa6ed9c | -2.94719 | -48.04797 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a11761-4b1e-3e64-8ad6-d88fddd40094 | -5.32208 | -44.69846 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3321e703-1662-3fd2-8a05-8c36afbc08ba | -4.73186 | -46.80223 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7156086-d0a4-365e-83f1-086ade3feb9e | -3.30662 | -53.37052 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 201c8019-5d69-389d-88fa-33cecd7550b4 | -3.01883 | -48.03145 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01b32d61-e38d-38b9-a9bc-c23c25b4f030 | -6.07788 | -44.14613 | 2024-12-17 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 332858ce-24a1-3250-873d-cb2fe11d7144 | -3.99605 | -46.57063 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a56726a-f408-3de9-ade0-8b32320ccc93 | -5.59363 | -43.2871 | 2024-12-17 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84b74133-02cc-30e2-b5dc-f4fd0ae3b5ab | -4.0445 | -46.9123 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f3ad7da-460a-3e3d-b3a1-163a53d1fed5 | -3.37749 | -52.80764 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b9766cf-2237-3c76-8b8e-c401c3f60ba5 | -4.01227 | -46.89857 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e603a99-3a00-365f-bd54-4dbcb9c984f4 | -4.96538 | -44.96716 | 2024-12-17 04:44:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29a59b7b-9cf9-36ae-b402-5e43fd12342d | -4.39719 | -41.43468 | 2024-12-17 04:44:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ebd26471-d263-3001-a996-930c7cf7350c | -2.54603 | -48.38016 | 2024-12-17 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 428936aa-a6f2-313e-b771-b8b3a7c6c41b | -5.13818 | -43.23584 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a91074c3-0691-34b6-aae5-76bde372cfb5 | -3.30432 | -53.36171 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be6c6fed-df08-3c35-b128-620081f216e4 | -1.08875 | -48.21296 | 2024-12-17 04:44:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93e89d8e-1488-3688-9d9e-1e5dc39030bc | -3.15273 | -53.17251 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da4ffddb-4093-363e-a07a-62c26738da27 | -5.21709 | -43.297 | 2024-12-17 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3be1fd33-2a62-301c-8cf0-7af92c7fa3d8 | -4.09686 | -46.82018 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 528567ee-1396-3da7-8d1f-8f1bdf7192ea | -4.89379 | -44.17511 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64294d87-a140-3820-b3b1-58058b762c91 | -2.93028 | -52.71618 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ead817a0-6fed-3442-a0b2-e27fb225c86f | -2.17966 | -53.74253 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ffecc2-b559-3474-9dcd-5caf9b4c3ea7 | -4.96531 | -43.72082 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3e77e93-c13d-37f2-a5fd-61489aeafe04 | -1.28525 | -53.18461 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d9f3bfc-e575-3508-96d9-dd704eb467ba | -5.98349 | -41.57077 | 2024-12-17 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1806b41e-1925-35ef-a8dc-286620db9793 | -3.9865 | -48.39923 | 2024-12-17 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33309d0a-7168-3788-872d-a441089a1c9d | -5.08704 | -43.90434 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 88b891ac-be49-38fb-ba57-3edc24a95439 | -3.87217 | -47.03547 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcbed38d-4683-3572-b8ce-fbb7119966a8 | -3.30794 | -53.36923 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e05fc7-a1a1-3052-95cd-0a955fe6f185 | -3.53119 | -54.69035 | 2024-12-17 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a36d6e64-2b90-3e3d-9753-2e1356f5e447 | -3.13841 | -48.60832 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d329b605-1a5e-372a-aef7-4075b4a80188 | -2.05325 | -46.665 | 2024-12-17 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ee8903-c4a8-3011-824e-666adbaca07d | -4.36761 | -46.07061 | 2024-12-17 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99b69c14-81bf-3377-9e86-d75b74ba131e | -2.57397 | -49.40729 | 2024-12-17 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11aeb918-4b46-35ec-92b5-a538666f814e | -1.32329 | -50.6481 | 2024-12-17 04:44:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dfc0177-db7c-3d6f-b748-e518071a4cf1 | -3.7666 | -47.17084 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d348e85c-18ec-3050-9254-88ed20708e6f | -5.06119 | -46.39547 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7316a1f6-f7e3-3f2f-b2c4-cdb627d0f3c5 | -4.62167 | -46.31823 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39a38e6f-ec1f-3b14-98a4-6d3216dcfe09 | -0.25655 | -51.50075 | 2024-12-17 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c61763e3-f68d-303d-b980-df36e61c1d28 | -5.62452 | -44.83727 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c110ddca-b0dc-392a-b7f7-fbe69a73a0be | -2.00484 | -54.32451 | 2024-12-17 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1e7a0f8-d077-3d76-89f9-2a46dab84a6f | -1.24954 | -47.83536 | 2024-12-17 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f29d66d2-8743-3760-aa5a-f6fbd5984aa3 | -1.37255 | -53.47637 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e0eef13-4c6a-3659-81bb-977b33f696d6 | -4.04382 | -46.9168 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80969525-56be-351e-91f7-3a12a9f92677 | -3.96048 | -47.02667 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
