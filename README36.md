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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a945901-fee1-32e4-91de-c1ea51ded71c | -12.78 | -50.57 | 2024-10-05 03:04:13 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca50cec7-efd2-3d24-bab3-eaaedaf186ad | -8.78 | -44.83 | 2024-10-05 03:04:34 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dee6f663-9412-346a-bfa4-e10d716354c3 | -8.75 | -44.83 | 2024-10-05 03:04:36 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c282c859-d188-3d48-a260-a941a33220ff | -2.9014 | -50.7142 | 2024-10-05 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 577c8f3d-7e71-3f37-b34a-adf645460802 | -3.3084 | -50.451 | 2024-10-05 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 304e00d1-bfb0-316d-a092-f8d9c762bd34 | -3.3083 | -50.4719 | 2024-10-05 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 85b116e8-a7b3-3250-975c-c2b917a48ac4 | -4.0794 | -47.9502 | 2024-10-05 03:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7ee7aefb-f801-3f96-9f11-9b9478159d0e | -5.8216 | -44.1196 | 2024-10-05 03:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 7631525a-5060-307c-a139-5003dba672ba | -5.8214 | -44.1426 | 2024-10-05 03:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4b106c33-7e4d-33f9-99ef-d0f324c940d1 | -6.9514 | -59.0666 | 2024-10-05 03:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 58e22369-b37a-3524-b9d8-a075c25c95af | -7.5193 | -63.2558 | 2024-10-05 03:05:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| edb1b64e-c362-3d5c-a51a-516fa4d4fbce | -8.7844 | -44.8085 | 2024-10-05 03:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 62a662a5-7ff6-3f69-8b82-b338be31ae45 | -8.7841 | -44.8315 | 2024-10-05 03:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 40731833-c015-3628-8d16-42fb0d1c9e17 | -8.7655 | -44.8106 | 2024-10-05 03:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 309.9 |
| b25c440e-447d-362c-a3dc-77ea6402734f | -8.7652 | -44.8335 | 2024-10-05 03:05:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 238.9 |
| 7ac45e4b-d4f4-3637-a337-b3cd0abd5923 | -8.7959 | -49.9533 | 2024-10-05 03:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 52138750-305d-3d2e-9bc7-1444857737a6 | -8.7957 | -49.9747 | 2024-10-05 03:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 688a8e28-9adc-396e-b0fe-4864b24434bf | -8.7772 | -49.955 | 2024-10-05 03:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7a38c39f-e139-308d-b521-bd332f865f84 | -8.9853 | -49.8083 | 2024-10-05 03:05:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 072affd0-86c4-37e1-9c84-5bd1f014550a | -9.284 | -65.4096 | 2024-10-05 03:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3124505a-b881-381d-892f-746ca89d5bd7 | -9.2839 | -65.4283 | 2024-10-05 03:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e90d63f6-2b21-310f-af60-37db6b59cdb3 | -9.1759 | -61.5794 | 2024-10-05 03:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1cc70e35-3aa8-31d9-a368-cdc95d088224 | -10.332 | -50.5109 | 2024-10-05 03:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ab5bd772-ef67-3241-b97c-82886eafb877 | -10.3318 | -50.5322 | 2024-10-05 03:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9e3baccf-9fe2-329d-9d33-9e0f09fedcc2 | -10.3131 | -50.5128 | 2024-10-05 03:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 8ddd3d33-617a-3262-aded-3f678057a5d5 | -10.3129 | -50.5341 | 2024-10-05 03:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 242.4 |
| 030a27f7-2558-3889-9923-4cba68cde21a | -10.2942 | -50.5147 | 2024-10-05 03:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 344548a0-02df-32f9-97f9-41564c13e590 | -10.294 | -50.536 | 2024-10-05 03:06:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| d0d6fb28-1ea9-3308-81d3-64f389eb564f | -10.4424 | -50.7336 | 2024-10-05 03:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 8fe41f08-1286-3cea-afcc-03ab88e226bd | -11.1155 | -54.2319 | 2024-10-05 03:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8a571950-56f4-358a-b709-8d79595ca69a | -11.0966 | -54.2336 | 2024-10-05 03:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2c73b09a-359c-3c2a-9e1d-e427dabca05f | -12.8202 | -50.5495 | 2024-10-05 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4c462b6f-5a89-3855-a60b-59882be29b11 | -12.801 | -50.5519 | 2024-10-05 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| fcd38c09-241f-3176-9708-c52f95493161 | -12.7822 | -50.5328 | 2024-10-05 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 4b0d9f93-1f0d-378a-b369-af6714c09170 | -12.7819 | -50.5543 | 2024-10-05 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 430.7 |
| 5a466b58-07b4-379d-b4a4-60acf2fe9cda | -12.7815 | -50.5758 | 2024-10-05 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| b9868f4d-59fa-3114-9294-c5260d21820d | -12.7627 | -50.5567 | 2024-10-05 03:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 9ecc0772-4921-3156-91d0-6bbe80b1a3b4 | -13.1052 | -46.355 | 2024-10-05 03:06:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 34092d0f-009c-3920-a032-7165a19e522d | -13.1362 | -51.1313 | 2024-10-05 03:06:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 88075f35-172a-33d8-b216-b05430557fbc | -13.3978 | -61.9376 | 2024-10-05 03:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 3ed73b50-74ca-3290-9930-b5aa18f688c5 | -13.3976 | -61.957 | 2024-10-05 03:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 165.2 |
| b4f19edc-032f-39d1-b56d-e4ad94614af2 | -13.3786 | -61.9582 | 2024-10-05 03:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b3fe91f5-9299-385f-9934-a764e629dfbc | -13.6328 | -51.2604 | 2024-10-05 03:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9d5f8d62-cb65-389e-9c71-872ad7e54ce4 | -15.5791 | -57.4532 | 2024-10-05 03:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| eae84c73-ac4d-30ff-bb25-b9433dbf9c0a | -15.5597 | -57.4553 | 2024-10-05 03:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b79294e5-e8e8-3258-8c55-9f21d08ca636 | -16.5544 | -57.2032 | 2024-10-05 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 04e78003-94ce-38c6-8715-f6706df9d7c0 | -16.5742 | -57.1805 | 2024-10-05 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 6c71e164-ea61-3b22-86bb-70c943939a99 | -16.5745 | -57.16 | 2024-10-05 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| d504dc57-6686-3792-8c2b-3e67f4089063 | -16.554 | -57.2237 | 2024-10-05 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 231.6 |
| 2cbab1c1-cab3-3c3d-b781-e942f2b26a0d | -16.5345 | -57.2259 | 2024-10-05 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 50b2b589-9b8c-3511-a5e4-72bd6c256ef6 | -16.6402 | -55.5243 | 2024-10-05 03:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 0b350fa4-93c3-307e-8172-d7c1f23597a7 | -16.6598 | -55.5219 | 2024-10-05 03:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 195b167f-994e-3691-82f7-09d0bbb1d244 | -16.6871 | -57.4536 | 2024-10-05 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 4cd8ecf3-1d62-3a11-8c4b-eb5b7c1f61eb | -17.0892 | -56.7709 | 2024-10-05 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| cc63d532-0b05-3be6-9039-ad5e489c5185 | -17.1085 | -56.7892 | 2024-10-05 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| a4bcb520-095e-3293-8f50-f9411fe5f09e | -17.1178 | -57.4244 | 2024-10-05 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 8ddd7f86-ea7b-38d6-a57d-90f269fbf064 | -17.1182 | -57.4039 | 2024-10-05 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.6 |
| 040f2b96-e1fc-3982-981d-3e92c1d1bf6b | -17.1375 | -57.4221 | 2024-10-05 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.2 |
| 05cd7049-ad84-3720-b0f9-47904a97dac0 | -17.1378 | -57.4016 | 2024-10-05 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 183.2 |
| 6397f707-afee-3025-a862-d0d60b5b68d8 | -17.1381 | -57.381 | 2024-10-05 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 77cbe375-cb9a-3fed-9e94-b17ccae934b3 | -17.1574 | -57.3993 | 2024-10-05 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 004f353a-7b0a-3c09-aca5-1b5ef04353b8 | -17.7112 | -43.793 | 2024-10-05 03:06:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c0e5e787-fa49-3ed0-a304-490ad8c518f9 | -18.5062 | -52.8193 | 2024-10-05 03:06:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| af281c9b-313c-31d3-8dcd-6d31e5e20eac | -18.5058 | -52.841 | 2024-10-05 03:06:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 501.7 |
| 9d4ec651-a2bf-3d81-8a38-a9ce45ffb61c | -18.5053 | -52.8626 | 2024-10-05 03:06:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e4e831b2-a26a-32c5-9ae5-3fe32ad1c389 | -18.4858 | -52.8442 | 2024-10-05 03:06:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 157.5 |
| df9148ce-dce9-39ad-9130-d69bf9428ccf | -18.8816 | -43.5785 | 2024-10-05 03:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| a3667caa-0699-3619-b095-9444c1372e7e | -18.8809 | -43.6032 | 2024-10-05 03:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.0 |
| e9a0503f-fe71-31f5-af06-0a8758d5c627 | -18.6981 | -57.2915 | 2024-10-05 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| a81d6eaa-aec0-3d57-9ed8-47f2ae0f7911 | -18.6785 | -57.2734 | 2024-10-05 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.3 |
| 656d0b66-a193-3f45-b32a-fde290082fd6 | -18.6782 | -57.2941 | 2024-10-05 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| ff9c2ae9-b9de-3cc1-83fb-aa8dcecf59ac | -18.6586 | -57.2759 | 2024-10-05 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 46030803-42dc-3048-812c-17c6027541e6 | -2.9014 | -50.7142 | 2024-10-05 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a7381f8b-ed26-3c9b-af32-61c5a22c824c | -3.3084 | -50.451 | 2024-10-05 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 871ebc33-0d34-3d01-9605-308eebbb3fd1 | -3.3083 | -50.4719 | 2024-10-05 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 9826b089-35fc-3e04-b5f9-2a052b4a4605 | -4.0794 | -47.9502 | 2024-10-05 03:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b52b57e3-02c5-3574-bce4-e8c754979e11 | -5.8216 | -44.1196 | 2024-10-05 03:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 05243028-2986-3481-abd4-89914ca3bb76 | -5.8214 | -44.1426 | 2024-10-05 03:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8a4befef-e33b-3f5a-bcd5-81ead69313b5 | -6.9514 | -59.0666 | 2024-10-05 03:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4d08eab7-30d3-3e20-92fd-6fab1817e4c3 | -7.5193 | -63.2558 | 2024-10-05 03:15:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 32c4373a-9562-324a-8b17-8cf199e65f8a | -8.7844 | -44.8085 | 2024-10-05 03:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 266.3 |
| db74a6f5-0721-3acc-9a0f-bda3b33872ea | -8.7841 | -44.8315 | 2024-10-05 03:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 217.5 |
| fcb8928a-1309-3a9f-945d-151e4c73466f | -8.7658 | -44.7876 | 2024-10-05 03:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 31c51bf8-13a8-3ba0-9e4b-ab5483973628 | -8.7655 | -44.8106 | 2024-10-05 03:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 438.6 |
| b49001f9-1587-3ad0-a8a0-f410f2066d71 | -8.7652 | -44.8335 | 2024-10-05 03:15:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 358.2 |
| 4fc8c1e8-cb8f-3246-b462-be23181c779b | -8.7959 | -49.9533 | 2024-10-05 03:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 66c6f7fd-7abe-3ab0-bfac-00ff1e433d62 | -8.7772 | -49.955 | 2024-10-05 03:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6e2062e7-7934-36fc-badc-3fa3e557ad89 | -8.9853 | -49.8083 | 2024-10-05 03:15:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a8b365d4-5c40-3c0d-a28e-02063392677f | -8.9851 | -49.8297 | 2024-10-05 03:15:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 62e859eb-543f-3054-b69c-7cdaef59d444 | -9.1759 | -61.5794 | 2024-10-05 03:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 39a9568f-72f1-3b38-a616-a03d70eaee89 | -10.332 | -50.5109 | 2024-10-05 03:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 82afacc8-9a86-3b54-80d4-b2c6aa961118 | -10.3318 | -50.5322 | 2024-10-05 03:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| da65b913-e4d9-3a4e-832f-793aede31e63 | -10.3131 | -50.5128 | 2024-10-05 03:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 570271c5-784e-3d90-970e-3dfd722be42e | -10.3129 | -50.5341 | 2024-10-05 03:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 45a36798-be2c-3b08-a384-b1e678b149f6 | -10.2942 | -50.5147 | 2024-10-05 03:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c030ab70-9911-3b33-8fe0-310e8c46fab0 | -10.294 | -50.536 | 2024-10-05 03:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| ae4fa013-6b85-38d2-a987-c70017c0af5b | -11.1155 | -54.2319 | 2024-10-05 03:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9ab479ab-d9f3-3b1a-91da-93b60bb3d6a8 | -11.0966 | -54.2336 | 2024-10-05 03:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 96ede547-4fe7-3520-b422-9eeb7e753c13 | -13.1052 | -46.355 | 2024-10-05 03:16:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 2502a017-b765-3328-9674-204d7e36e6fe | -13.1047 | -46.3778 | 2024-10-05 03:16:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |


[Clique aqui para ver as próximas entradas](README37.md)
