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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1549a52-2cb5-3b46-9402-0bbbfbcde501 | -6.6614 | -45.56126 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a29f13e-f126-3694-938b-5cdb1f2cba44 | -7.68694 | -48.86189 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce1d35d6-c0f1-3dd4-a2ed-c316fca59d9c | -8.10732 | -50.15901 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b66159fe-6d51-3a4f-96e8-aed1ffb1c35a | -5.18427 | -45.1734 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d1c52c5-0575-37f4-9eca-764bc3da18c0 | -5.14888 | -44.70485 | 2025-09-15 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11bcaa4e-0b7d-3355-bdf5-362f1a76da99 | -6.25626 | -43.46421 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a150294e-3050-320f-9db9-3f5836731ab1 | -6.97669 | -38.45295 | 2025-09-15 04:19:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a01adc9d-e2ac-341f-b144-31dfb8f54d19 | -3.6534 | -54.06155 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ac2e876-001c-3ca9-9fee-70d16baefc2f | -8.02088 | -44.96585 | 2025-09-15 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e69f9bc3-f791-3096-a328-22a1c8857a95 | -9.23504 | -45.66413 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0376e6b-d553-35d9-ac61-c920734130e9 | -8.07824 | -44.50867 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1452bf48-045f-3044-b2db-a8e3ee42de2d | -7.3562 | -44.29494 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a80a98a-4cd3-34ea-82a4-1e56744923b1 | -7.05924 | -44.6754 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abc2498d-84fd-33be-85ab-2f8dab6a4b00 | -8.11526 | -50.1606 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 246ed9ab-3c79-351c-a0f5-a5d292a9f3bf | -8.97937 | -45.81881 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa21ed01-3203-31b7-a175-897fb1ebd5cb | -7.80303 | -46.13211 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d30b7e37-1740-3b93-b6db-b0dfaf8b79be | -6.77278 | -44.72194 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e878c197-022f-3f31-98bc-01aa42e0fa67 | -6.98131 | -44.54219 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1b34059-60db-3757-b307-07e735d704a3 | -6.77554 | -44.72591 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eacdec81-5d7b-3ac3-8c8e-c8d55893b30d | -7.8789 | -43.56485 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| fcf98909-7ad9-3943-b4b5-414ffc86f272 | -5.76727 | -43.92582 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cd1fd02-cea5-3b99-9922-ca206a48854b | -8.11074 | -50.16309 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44949899-dc6d-352f-a373-3e0f7e885680 | -6.55239 | -43.99456 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6779fe99-8f3b-3849-835b-903ea13f6c13 | -7.52095 | -44.70197 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7404045-af21-3f46-baf1-ff1586987ac9 | -8.4192 | -44.96509 | 2025-09-15 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ca786dc-5c9a-374a-8914-a85303f11eb7 | -6.16712 | -41.20244 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 65428b6c-0d1c-3b96-8ee3-d223dae15898 | -7.98536 | -45.66992 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57f0f88d-11c5-30ff-a905-26b17e138680 | -8.76873 | -46.07434 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fcd6bca-a423-300c-ae45-4b52a85a74ef | -6.19026 | -43.47583 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 399d084e-12ca-378b-a4dc-494fb353c755 | -7.99563 | -44.81941 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da65344d-4a86-3a14-9527-1f8c95d0c20f | -6.20632 | -55.63035 | 2025-09-15 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c6d3e9e-b4fd-3d44-a548-0e81822b4fb4 | -6.65062 | -44.71999 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e896b64-a32c-3107-84f8-b74e75212b21 | -7.69431 | -44.6794 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0d32e47b-bd16-3299-b135-a08204fd1347 | -5.74772 | -43.91879 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcd7bed3-9fc4-3f5a-ad0c-b118358fe9f9 | -7.64079 | -49.74018 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09bbff3d-7c20-3177-91e7-c882cd14ef64 | -5.97201 | -45.85407 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8de54fd2-95e1-34da-a261-69f811ff4694 | -8.97497 | -45.82525 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18cb845f-d53f-3f79-ba5c-41753ef563e8 | -8.91607 | -45.46371 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ff4ade2-e2a3-3655-91b0-32023a606f89 | -7.79835 | -46.11997 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c70a19d1-e4bb-3966-acc8-6cc556b2dcee | -8.62164 | -45.73288 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6abb5f20-f29d-3f83-8d67-deb42fa236b3 | -3.52171 | -49.24874 | 2025-09-15 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dbf0ff3-7079-3923-b091-613d9b20b1a9 | -8.15192 | -43.65406 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad6f21d5-cb30-3b4b-b7b3-41248b7f2841 | -5.9685 | -43.21098 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f38a9cf2-14d4-3e71-87f0-d58d6c99ffc7 | -6.41197 | -46.93405 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31d3619c-62f4-3750-9468-95d71fe4ac61 | -8.9189 | -45.48897 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c61dc20-aa93-3db6-85ac-9b2471f1bb76 | -8.64753 | -46.3654 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28d33311-1940-33a8-b92b-beef263df19f | -5.70574 | -43.40158 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06bd07e1-0769-31f8-9cd1-472a0126cea9 | -6.7018 | -44.12835 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bf07614-c012-3336-9a06-cd944c2917da | -4.03849 | -51.03173 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ed98521-cd97-3b0f-be55-ec53e8eeb39c | -2.81404 | -48.62556 | 2025-09-15 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12af6cdb-23f9-3376-a9c2-ffcfde3c3b23 | -6.17553 | -41.19335 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 48188e67-61e6-3499-80ba-4e0abfbc2eac | -8.41777 | -47.22121 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5bac3be9-51c5-3a12-9be4-3276e4dcf649 | -5.92967 | -43.22747 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6dd5f52-75d3-30a5-afdd-d879d82dd16a | -7.98746 | -44.85014 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d29ec07c-4ca2-3d3b-84c1-c12fc764d247 | -9.05408 | -47.02042 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75bd499d-6cba-3829-9f64-6cad9bd6bdc2 | -7.85198 | -43.85544 | 2025-09-15 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44020a08-0df2-3d5d-bb41-9658720bfc43 | -6.05708 | -43.56808 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20227ed6-0d20-352f-a659-1f2a829c8522 | -5.95432 | -42.79468 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dd2fb860-72c2-34b5-bf8b-b8fcaea6eda6 | -7.68454 | -45.13562 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12aaf128-ce8a-3504-9969-a9393942ed85 | -8.97054 | -45.76746 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9906002d-424d-3d58-a6c5-ac718ffc7a72 | -8.96669 | -45.77041 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dbd2787-b61d-361f-a793-22d70f5d2234 | -5.84627 | -44.162 | 2025-09-15 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e49b8ec-f0aa-3020-bc33-7896426ff7fe | -9.01854 | -47.02596 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f351415-ba0b-3a62-ad9e-0f1a7a38e8df | -8.10282 | -50.16137 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcd0f8df-8eea-371f-9ebc-85835cba487d | -8.98598 | -45.81988 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6eb05ff-4054-38e5-b667-d85a7e5c058f | -7.47507 | -44.97461 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc9c29c0-12f5-33d3-b090-869213a4c084 | -5.48069 | -44.69384 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c7e0f7-039a-3b97-9f7a-8f1d6d6e206f | -8.96237 | -44.44175 | 2025-09-15 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2428dbe7-bc21-3886-8d68-c65308611d35 | -3.22 | -47.12648 | 2025-09-15 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bf95ff2-4121-3bfd-946c-f99e3a660ef9 | -5.84904 | -44.16597 | 2025-09-15 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4a3be2f-df35-31b8-855f-ee04be0e3380 | -7.48353 | -46.14986 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8a2d665-a452-3622-9ded-849c496e2035 | -9.23119 | -45.66708 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d03468af-a0fd-3fb6-bf3f-f3a2c5527d7a | -8.91231 | -45.48792 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f762b1ee-3c34-3315-be3e-4689719c0dd2 | -3.55531 | -49.04287 | 2025-09-15 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e0029fa-b823-3f30-ba5e-06c3b51abd31 | -9.00586 | -47.06162 | 2025-09-15 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba07e894-9f5d-34b8-b478-ffb5f7305d16 | -8.63145 | -45.69528 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77c343a9-4b73-3c6f-97dc-a0cb48578809 | -8.0777 | -44.51219 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b17ae14a-a76a-3599-bd0a-2a7ca5dc5247 | -5.48123 | -44.69039 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4fcfb67-4cba-30bc-8e4a-97398d6fe53f | -6.44315 | -43.31301 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef65c9d7-d103-3601-9657-fa89e173fd08 | -5.15131 | -46.00568 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e0770d87-e48c-3f0a-bbd0-b57283572e6e | -7.86956 | -43.57062 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77b319d3-7ba7-3db0-a786-7beceecc6c2f | -7.88063 | -43.57627 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| af85420f-eddb-3d90-a4b4-62d8198550be | -7.74675 | -44.78048 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 355068f1-c406-30ad-82e7-2099929128e0 | -8.98377 | -45.81238 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3117d642-0963-368f-b53d-44a548f807a6 | -7.69101 | -44.67886 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9f15280-63ef-3df3-806f-404e6f1c4389 | -5.25737 | -42.60266 | 2025-09-15 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 487ea1c3-c99d-3bfb-aa71-5acef063d078 | -6.67022 | -45.54837 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b36aadf6-d91f-35ca-a5a3-1f1c08112e06 | -6.18178 | -41.17644 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a2075a94-e67a-36e5-aed2-ed7026b76a63 | -4.85771 | -45.73252 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e6ddf4a-a25d-346c-8645-b912c611ffc0 | -7.79226 | -46.11535 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e902bb-587b-3ae5-bcee-40f5b72a55fa | -5.0926 | -41.15496 | 2025-09-15 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e066a483-f6b7-300c-9460-f55c98a487fd | -7.48415 | -46.1246 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8254792-0725-3f9c-9aab-661e573cdd03 | -7.35897 | -44.29897 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ead1c01-8d54-3d23-8a32-d096c17607b4 | -5.82372 | -43.4925 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f3c3214-ace6-3fe2-b574-37a2507d5403 | -7.51508 | -44.36665 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cea76e6c-bde9-3fcc-a5c4-2b1b7c864235 | -7.38866 | -49.98978 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d554e580-3291-3e17-bb56-43593b577cfa | -8.91564 | -45.50977 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c6dd680e-16ec-3d77-b866-daa0cd0d1096 | -7.30294 | -46.57518 | 2025-09-15 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 450a6c00-c636-392e-be9e-bb66edf89b4c | -8.63586 | -45.68884 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6a88bd51-072c-36f8-9009-d91ed6899e16 | -8.89369 | -46.16681 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
