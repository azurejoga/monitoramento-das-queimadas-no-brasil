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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9431fe5d-8fa1-3b2c-b426-32172bbd4091 | -3.341 | -47.306 | 2024-10-13 02:05:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b02e3f67-de49-3a77-b3e5-00066827af59 | -4.1148 | -48.2515 | 2024-10-13 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 39f416be-67b4-3efb-9981-71990480051d | -4.1149 | -48.2299 | 2024-10-13 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 56e68ad1-2eec-3421-bcef-156e4898c6d1 | -4.3985 | -44.4881 | 2024-10-13 02:05:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4871a59b-d4d0-3d22-afa1-a49800a0c5a1 | -4.3986 | -44.4652 | 2024-10-13 02:05:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6667aa90-5415-3814-89e8-900c5197d834 | -4.7188 | -60.7882 | 2024-10-13 02:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1bb5a7d1-3bfe-3d0c-be46-a6c73a0688e7 | -6.1301 | -47.2664 | 2024-10-13 02:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d6b8bbdc-f379-3034-b1be-2a5f696fc69a | -7.6627 | -47.3229 | 2024-10-13 02:05:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 09e4ce34-ea7a-3035-b0db-522e7492b996 | -7.6815 | -47.3213 | 2024-10-13 02:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 77a3ad50-695e-3dc2-8fbd-ec1b56ecded6 | -7.6817 | -47.2992 | 2024-10-13 02:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| a4af9842-86bb-302f-bda7-8fe75f8b1538 | -9.7359 | -64.2295 | 2024-10-13 02:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6edcf85b-8232-3936-bfdc-a17c1d00bf27 | -10.5283 | -49.9564 | 2024-10-13 02:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 97ecf04c-d0de-384d-8a84-1e69ec59e835 | -10.5281 | -49.9778 | 2024-10-13 02:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 812819c2-7d46-3164-bdff-3b0b3b414795 | -10.5094 | -49.9584 | 2024-10-13 02:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 354db86f-e07a-343c-a2e8-bc30e210b703 | -10.5091 | -49.9798 | 2024-10-13 02:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 8b3227f7-8583-33b3-a899-f4c0f84c3be1 | -10.9311 | -44.6789 | 2024-10-13 02:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 890f01d5-357b-326e-8233-9a667db0bbe4 | -10.9315 | -44.6557 | 2024-10-13 02:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| ed7d551e-eb30-3952-8493-04a47fcef272 | -10.9502 | -44.6762 | 2024-10-13 02:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 39358bca-1a23-3ba0-9316-3f2a37fa287e | -10.9506 | -44.653 | 2024-10-13 02:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 4b7a0b99-e1e7-31d3-b3d4-9bd57259f35e | -11.6334 | -48.3736 | 2024-10-13 02:06:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a5d5029d-aa04-3d78-93ca-8145c68c70df | -11.7308 | -64.9769 | 2024-10-13 02:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c7a6d604-cf26-3af8-a5cd-75caee8476bd | -12.2754 | -47.6473 | 2024-10-13 02:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 542773d0-808d-3ce3-8394-c41771a23c43 | -12.3982 | -63.7284 | 2024-10-13 02:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 1c22b528-4d16-3374-ba60-69733163d20c | -13.1475 | -62.3215 | 2024-10-13 02:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 40d69d3c-530f-38c8-8e50-9ee3a442bb0f | -15.6419 | -59.9767 | 2024-10-13 02:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| cad7f396-737f-3240-8c84-f8ae29d15a99 | -15.6103 | -59.4217 | 2024-10-13 02:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 79b2b8ef-4bad-3cba-8648-366b88559fe1 | -16.9995 | -57.4791 | 2024-10-13 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 97caa98b-d21e-3b59-a48a-dd18e8ed8838 | -17.2639 | -42.6527 | 2024-10-13 02:06:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 38122f90-161d-3d43-8b0e-8304466186f6 | -17.0823 | -56.0076 | 2024-10-13 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 10a4eda9-ff6e-3f3f-b28e-8e17a4688420 | -17.0819 | -56.0283 | 2024-10-13 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| c59d7ea9-b54d-3fc9-ab9c-80f0c53bf0fd | -16.9998 | -57.4586 | 2024-10-13 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 294f14b3-8b4d-38bb-b1ee-7f5011ac33ea | -17.196 | -57.4357 | 2024-10-13 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| acf2ec3d-818a-3ba8-92cc-9463ebc62bce | -17.1957 | -57.4562 | 2024-10-13 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 194.5 |
| 07fe4245-5c3c-3e35-90d5-c2e1aaeadec5 | -17.1954 | -57.4767 | 2024-10-13 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.4 |
| 494db930-d6e9-34cc-a366-ea2ae7e51e10 | -17.1764 | -57.438 | 2024-10-13 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 03d93860-04ff-316a-9f9f-daf56b515256 | -17.1761 | -57.4585 | 2024-10-13 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 204.2 |
| 7ee58d8e-c619-39e3-ad87-8adc74cd637f | -17.1758 | -57.479 | 2024-10-13 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 147.6 |
| 593b0376-45df-363e-bee4-183d80049055 | -17.6474 | -56.2876 | 2024-10-13 02:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 61b02571-334a-3f82-a737-9b0eacb449c7 | -17.6478 | -56.2668 | 2024-10-13 02:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 35f14d20-4196-3151-be42-a11637396006 | -17.6672 | -56.2851 | 2024-10-13 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| d69cef09-9575-367a-958a-447eec2d7308 | -17.964 | -57.3843 | 2024-10-13 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.2 |
| f8378a6b-ad5c-3c20-9236-2b198ea0db3c | -17.9643 | -57.3637 | 2024-10-13 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.0 |
| e474a977-b3c4-3c86-a9fb-38f56d9d0f51 | -17.9837 | -57.3819 | 2024-10-13 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| cb74f33a-f3a1-345c-9408-4456661df938 | -17.9841 | -57.3612 | 2024-10-13 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 14f76759-31e1-3afe-834c-f213b2698a24 | -18.23253 | -56.49878 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.9 |
| f2401f5c-f3d7-3459-a426-c38d07556930 | -18.22609 | -56.46559 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.0 |
| f406b10f-9131-302f-a9c2-8ee35a635898 | -18.22334 | -56.53519 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.7 |
| a2c1c8f7-9e69-35f9-aab8-6d62bbdf368a | -18.22318 | -56.50606 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 967b287e-7f75-3a7b-9d4f-5ebadce4df0b | -18.22 | -56.57543 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| ccdc46f3-bcc4-3465-8fee-d46d11239502 | -18.2196 | -56.43221 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 9829bdbd-f58d-3805-aa8b-b4f47c0eece7 | -18.21694 | -56.47282 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.5 |
| f4370a7e-3335-30e9-9b86-52839327c7df | -18.21691 | -56.50221 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| b8d3dd84-b704-3f91-86ef-0216c59fe620 | -18.21419 | -56.57138 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 61309d34-0af6-3765-9b98-932ad5f7855e | -18.2138 | -56.54258 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 2a153a76-47e0-3a1b-b073-26d5ef16177b | -18.20445 | -56.57885 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 61cfec5a-33a9-363e-9283-87f38bb5a9b6 | -18.12978 | -56.31063 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.0 |
| c0662ad9-8e41-39e2-a0bc-933c63897910 | -17.98132 | -57.35555 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 89860329-7402-3ff8-b774-bb918c29b164 | -17.97192 | -57.38758 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 9b79465c-655a-3ae4-ad8c-d860e6979624 | -17.97113 | -57.3824 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 7734f5e0-3b54-391e-8a9d-543c8410eba3 | -17.96655 | -57.35871 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 1569d77b-41c7-3fdd-9b00-10a61a039e88 | -17.96556 | -57.35358 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.6 |
| 11737102-8798-304d-b7ef-89dd3ef01c8c | -17.90191 | -57.3423 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 624.9 |
| ed72f409-02b6-3523-a265-dfa1f7bb51a8 | -17.8978 | -57.31969 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 274.0 |
| ee9bca52-33cb-3847-a57d-69e1eece047e | -17.89634 | -57.31318 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.2 |
| 1ff2bf71-574e-333c-95f1-2bbb26beb4b4 | -17.88709 | -57.34543 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 32ea8670-5699-39cb-bd8f-797ead42313f | -17.86417 | -57.38736 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| e18178b6-7aea-3ec6-b8fd-87e2f9ee340e | -17.85875 | -57.35838 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 0b1d785d-62f2-3737-b74f-cc9fdfc20779 | -17.8494 | -57.3905 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 7bc86390-b60c-3f5d-9dcd-f61db6b3b4f4 | -17.84394 | -57.36151 | 2024-10-13 02:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 213cda0f-0784-3312-a50c-22d3b5552938 | -17.18614 | -57.45737 | 2024-10-13 02:13:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 203.0 |
| a90793d9-15d1-3b1d-bb68-988a28aa00fa | -17.18437 | -57.45098 | 2024-10-13 02:13:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 190.8 |
| 23f27c5d-23aa-32ad-8b26-1d9fabeaf1a3 | -17.11335 | -57.47794 | 2024-10-13 02:13:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 60aa432f-ac9e-3871-90e4-b8ca200ac16f | -17.00339 | -57.47033 | 2024-10-13 02:13:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 9ec9ef1a-0670-30de-8a1b-71cbaa144c22 | -17.00009 | -57.447 | 2024-10-13 02:13:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 0f9ac5e0-1bc2-3a91-80c1-90559810208f | -16.99056 | -57.47982 | 2024-10-13 02:13:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| a551b295-ce45-3f78-8499-1d5aa8d5f9b0 | -15.95333 | -59.13002 | 2024-10-13 02:13:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8efcd11a-099d-32ad-906c-ce3a7bc6188d | -15.94904 | -59.10581 | 2024-10-13 02:13:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 883cad14-8162-3502-b32b-c8d3ffcc996f | -15.68662 | -59.34269 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 636af3ff-38e0-3dd1-b140-561790530ef0 | -15.65315 | -59.97552 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 11bd746c-7c92-3d31-9637-a036890ddea6 | -15.64042 | -59.97792 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2c9cef29-7710-3325-a534-ac2167996fec | -15.62768 | -59.98023 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6d2a9263-7be8-302b-9851-335c94ea6208 | -15.61547 | -59.43975 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 556dc5a1-0649-3aaf-921b-7d14e1d3d105 | -15.61458 | -59.45661 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b2ba06b8-e131-367b-9832-50b5d23f26c8 | -15.61167 | -59.41735 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 056f9092-fe72-3832-a974-b8df7c9d82e5 | -15.61085 | -59.43563 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f9dbf4c4-b828-3154-a2f9-b487fdd9745f | -15.60671 | -59.41231 | 2024-10-13 02:13:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0d3b369d-7da8-3013-b4ea-95c72e43a584 | -15.1768 | -59.73055 | 2024-10-13 02:13:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c78099a4-c561-33ca-a769-4a8c49c2c774 | -15.17354 | -59.72478 | 2024-10-13 02:13:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b85b8f90-0824-3e04-ac12-2a799148b06b | -13.73164 | -60.60765 | 2024-10-13 02:15:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 34ecd329-1a3a-3cb6-aa17-e31e527247c9 | -13.72233 | -60.62941 | 2024-10-13 02:15:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 173.0 |
| cd87d3cc-de5b-3e07-88ab-c35f671a58d0 | -13.71906 | -60.60996 | 2024-10-13 02:15:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e81c64cf-5ad7-3554-8167-06f54c8cf84f | -13.0094 | -62.47371 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8d47dae1-5c46-31a0-8f60-c36d9969b07d | -13.00072 | -62.49027 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9118566b-d100-387f-a71b-f9e86cbca06f | -12.99838 | -62.47569 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 11f29834-8d89-3a8a-9f9f-9a15d9252906 | -12.992 | -62.50643 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6a683353-4e67-3583-b4df-5d03e3163f74 | -12.98062 | -62.73285 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8e1b7901-8620-3fe0-a210-5d21a53efc08 | -12.97844 | -62.71888 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 5d64a203-d483-334a-b89a-c88ccc3e6144 | -12.96774 | -62.79199 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3cb70c13-0882-3d15-8b70-daeb1f2e1c76 | -12.9385 | -62.5361 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 35872318-3b65-3ab7-bd33-c74f679bcfa0 | -12.92521 | -62.52353 | 2024-10-13 02:15:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |


[Clique aqui para ver as próximas entradas](README29.md)
