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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04971cce-c3e4-3fc6-9458-9612e53aee66 | -4.03948 | -54.22683 | 2026-10-02 07:26:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f6c512f0-18c1-3a83-9b50-f6f53df16994 | -6.9132 | -59.2806 | 2026-10-02 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9524a00d-5ce9-368d-bd2e-e3cea475ce83 | -11.1611 | -44.6234 | 2026-10-02 09:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ad8e69ea-9809-330c-9144-5a95a57d7655 | -11.1615 | -44.6002 | 2026-10-02 09:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ada089a4-3de5-3cae-a20c-210494978644 | -11.1611 | -44.6234 | 2026-10-02 10:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| ee517afe-9445-3868-a072-b7bf55fc4fee | -11.1615 | -44.6002 | 2026-10-02 10:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 45ef277f-50e5-3481-8051-a4713019c68e | -11.1611 | -44.6234 | 2026-10-02 10:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 3b79d0d0-9dfe-302e-ab27-df8db6d316f6 | -11.1615 | -44.6002 | 2026-10-02 10:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 3f06928d-ab87-35f1-9b3f-71d3c8f26304 | -11.1615 | -44.6002 | 2026-10-02 10:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 37438971-c072-34cc-8e5e-87f4638160e4 | -11.1611 | -44.6234 | 2026-10-02 10:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| afe68c86-0990-3cc2-bea0-95299c37400a | -11.1611 | -44.6234 | 2026-10-02 10:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| d1f9898b-a693-3b8a-841b-d5678b719209 | -11.1615 | -44.6002 | 2026-10-02 10:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 19510418-9744-358e-bca3-cd645aacecf4 | -11.1611 | -44.6234 | 2026-10-02 10:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| f91eb232-f8e7-3581-98c9-b1005b7a8af1 | -11.1615 | -44.6002 | 2026-10-02 10:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| a734434e-c719-3499-a75d-33123fb4bbe0 | -11.466 | -41.5304 | 2026-10-02 10:50:00 | GOES-19 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 73c055f6-e896-376c-b635-dfdd8ce6a809 | -11.4315 | -43.3884 | 2026-10-02 10:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 157ee456-0e54-3bab-be85-10c1957eae38 | -11.1615 | -44.6002 | 2026-10-02 10:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| d151b7cb-5045-344e-9bd8-72c9370fa031 | -11.1611 | -44.6234 | 2026-10-02 10:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 4b1be124-df8d-3a13-bed2-2989e25f1156 | -11.4311 | -43.4121 | 2026-10-02 10:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 61b27583-179e-399f-bb87-a596ec8b6993 | -11.4315 | -43.3884 | 2026-10-02 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 90652547-40e3-371b-a9b5-bd1731b365da | -11.1615 | -44.6002 | 2026-10-02 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| d79cf10c-4652-36e6-8670-63955dc3805f | -11.4503 | -43.4091 | 2026-10-02 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 174c650a-b382-3f3d-a6aa-5d2a9f292e42 | -11.1424 | -44.6029 | 2026-10-02 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| dcf1238a-18ab-32f9-959a-6399a079cc9e | -11.4311 | -43.4121 | 2026-10-02 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 658ec409-508e-3d74-9b4f-3d3ae24ba066 | -11.4123 | -43.3913 | 2026-10-02 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 17a24bf7-99ac-338e-9155-70ce43bf2060 | -11.1611 | -44.6234 | 2026-10-02 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 48903b5a-318a-3cda-b239-82bf929a6c9a | -11.1615 | -44.6002 | 2026-10-02 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 237.4 |
| e21e7e9f-1660-3f52-9a55-d9b4e4bbfd50 | -11.4123 | -43.3913 | 2026-10-02 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 7693b5bc-05ae-3023-950a-5a522ecd300c | -11.4315 | -43.3884 | 2026-10-02 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 6356a759-eed4-322c-aa4e-51a83a23cd5c | -11.4311 | -43.4121 | 2026-10-02 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 241.7 |
| 3fcdf737-8b82-34cf-923e-21061da5930d | -11.2629 | -44.2598 | 2026-10-02 11:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4dc5cf73-76d2-3fef-bd33-6097d150dd2a | -11.6579 | -43.5899 | 2026-10-02 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ae605d67-8bd6-38a9-a0f8-eaaaa6778d9b | -11.1611 | -44.6234 | 2026-10-02 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 267.4 |
| 2b602251-4632-3039-b8da-885f5a399c46 | -11.4503 | -43.4091 | 2026-10-02 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 3d1b135f-81ea-3778-a7a8-a8b7e1b7c3af | -11.4119 | -43.415 | 2026-10-02 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 434c37cb-ea91-33ce-964e-590fe7b88d78 | -11.7541 | -43.5749 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| acce2da4-10f7-39dd-8626-e5ffacc71d87 | -11.4119 | -43.415 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c9802aae-ce4c-34ff-8d4b-cf54199c3e4b | -11.6771 | -43.587 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e9239039-3032-3cda-9300-c2f2767fa188 | -11.4503 | -43.4091 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 283.7 |
| 9ae5a030-a998-3f7b-a185-116c221bf094 | -11.6767 | -43.6106 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 558ecfcb-7d02-3dfb-9d58-f2ba18eef857 | -11.4311 | -43.4121 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.1 |
| a169016a-6431-30c6-8f95-ec51f9e1aea4 | -11.4123 | -43.3913 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 74378121-98bd-3e9e-8d20-5557c488ac7f | -11.4315 | -43.3884 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 2a180c52-7475-3960-b0cd-11a9acaf19ee | -11.6579 | -43.5899 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9d9cdd20-1072-3d41-aa99-e83d30e56442 | -11.6959 | -43.6077 | 2026-10-02 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5c81750a-f611-3871-8e28-0a3ab466f5e5 | -11.1424 | -44.6029 | 2026-10-02 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6ccfd493-9e9a-3f2c-843f-97b828cb7437 | -11.2629 | -44.2598 | 2026-10-02 11:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| cd7a1e06-460f-3d24-ad86-dd6787e62fd2 | -11.1615 | -44.6002 | 2026-10-02 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 6217d710-e473-3253-8c5e-f474e1d3d709 | -11.1611 | -44.6234 | 2026-10-02 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 366.1 |
| b6a46d04-f2ef-3f34-a9a5-acdbdfaf9a23 | -11.1611 | -44.6234 | 2026-10-02 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 13d66b0c-3747-3702-8468-525c49ee185e | -11.2629 | -44.2598 | 2026-10-02 11:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| d5d0352f-6320-3e21-820b-cfbef8d718b2 | -11.142 | -44.6261 | 2026-10-02 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 07d982bd-9bd6-3608-824a-72f39a712992 | -11.1615 | -44.6002 | 2026-10-02 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 0201a356-975f-39ee-a7f1-7b8e65bee44a | -11.1424 | -44.6029 | 2026-10-02 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 27cbfe6a-aebb-3c07-b452-09ed52a0dbd6 | 2.55002 | -50.95379 | 2026-10-02 11:38:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ff278986-4ba3-314c-a2c3-ef6566d8deb3 | -11.7926 | -43.5689 | 2026-10-02 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| eba1619c-1f96-3fb9-be2d-c6a22d6c37be | -11.2629 | -44.2598 | 2026-10-02 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| a3e93033-d98f-35e9-bca8-f00649f5349e | -11.1615 | -44.6002 | 2026-10-02 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 95bfdfe4-e06a-3063-b47d-b9e64e0346e4 | -13.8032 | -45.2521 | 2026-10-02 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 305.2 |
| c0703a6a-ee0c-323c-8c44-46bc4dd528b8 | -11.1611 | -44.6234 | 2026-10-02 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| acc729b4-0296-3a8b-9124-3cc80cd432ba | -11.7169 | -43.5098 | 2026-10-02 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 89b5be2f-7d04-3e20-a4d1-afe54a67fa25 | -11.1424 | -44.6029 | 2026-10-02 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| dc0af6ff-27b2-3837-864a-a93771f3e68c | -13.8037 | -45.2287 | 2026-10-02 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| f7a932e1-78d4-3fb3-adfd-8d156242ec6b | -11.6977 | -43.5128 | 2026-10-02 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a8335fc5-7180-3024-99b6-25b8770e0200 | -11.793 | -43.5452 | 2026-10-02 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 25370dcf-2d25-333d-9901-ccc0417f6f8c | -1.61862 | -47.6652 | 2026-10-02 11:40:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bfa07458-5b7c-38fa-b7c2-3059d4c84a59 | 1.74146 | -50.81609 | 2026-10-02 11:40:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 358c9893-bdb8-3d61-8d2a-5283a7041715 | 1.73692 | -50.82721 | 2026-10-02 11:40:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 26.1 |
| fb9d2b15-4725-3605-a060-248999f03c21 | -2.836 | -43.6559 | 2026-10-02 11:40:00 | TERRA_M-M | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a648d7d7-9b70-341d-9e05-e191f755e04e | -8.61798 | -45.40192 | 2026-10-02 11:42:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| a1e4d89b-c49d-3d8d-a12b-8cc0baa1b415 | -4.29287 | -49.08841 | 2026-10-02 11:42:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 73d16972-714b-343d-8921-6dd87261e656 | -9.16375 | -49.94904 | 2026-10-02 11:42:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eeccf8a2-3611-357f-ac3d-7b2d68be4587 | -9.77869 | -44.80644 | 2026-10-02 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 70a28987-2f97-336b-8d7f-39f36759d2b2 | -4.30245 | -49.08978 | 2026-10-02 11:42:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 593257ec-9492-3162-88c5-c248c7c310a7 | -9.78985 | -44.79696 | 2026-10-02 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| c688cdc7-429d-3d4e-83dc-50a28f1fd7b0 | -9.16533 | -49.93868 | 2026-10-02 11:42:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ec0cc5d5-5b47-31f6-81bf-c12f41589ae0 | -4.30094 | -49.10028 | 2026-10-02 11:42:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fe74d672-07ed-3305-a211-cf171fdae366 | -8.45581 | -48.69519 | 2026-10-02 11:42:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fd25f0b3-4ebe-3726-ae30-910234b119b5 | -8.94675 | -49.24911 | 2026-10-02 11:42:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b06a7b85-6f3f-3c02-9578-620a656f0ed5 | -9.83078 | -44.80907 | 2026-10-02 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 9a3108e5-1c4b-3e52-9a31-5e0c58624f69 | -8.91782 | -49.25467 | 2026-10-02 11:42:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d1f6dfd4-d759-3cf6-9cdc-4bc420399b17 | -9.18676 | -45.69539 | 2026-10-02 11:42:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 880dab73-530e-3406-8722-ebf3730aa39a | -9.1234 | -44.74239 | 2026-10-02 11:42:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4dc491a5-61e7-3484-a669-7d65cde67760 | -3.42213 | -48.33397 | 2026-10-02 11:42:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 45caf073-c35c-39f5-9bf6-711ff8709697 | -9.08056 | -49.88835 | 2026-10-02 11:42:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7fe3c5da-74f1-3a66-a760-e48e4a9795d3 | -9.0822 | -44.97478 | 2026-10-02 11:42:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9230fb41-25a3-3788-a344-cf3dec20a8bd | -9.81965 | -44.81859 | 2026-10-02 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 32abf741-6e46-38c9-819e-0c2e6e43e8f5 | -8.61931 | -45.39211 | 2026-10-02 11:42:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6b83cba7-733c-36d4-bccd-677796d76596 | -6.09325 | -47.67904 | 2026-10-02 11:42:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e95f2d4b-f377-351f-8eb5-a483641618f0 | -9.15955 | -49.94229 | 2026-10-02 11:42:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2c7aa560-1833-395e-8606-3dbc1f88c185 | -9.82109 | -44.80772 | 2026-10-02 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 2bdfbe52-1eb6-3ee9-854e-434123a5091e | -9.07632 | -49.88114 | 2026-10-02 11:42:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a1b163e3-7689-3d11-ac2f-a1059c621cfe | -8.46482 | -48.69647 | 2026-10-02 11:42:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3fc4acdc-0a1c-3082-b43b-98cc09155419 | -9.82934 | -44.81991 | 2026-10-02 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3e8329dd-3d9c-3fe1-a595-32906da7b12c | -9.66603 | -47.66042 | 2026-10-02 11:42:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c2ddf94-8e5d-39b4-bd2f-48152bfb54f7 | -4.00237 | -47.5821 | 2026-10-02 11:42:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6981e027-5b79-33c8-ab92-e076a94874a4 | -9.78838 | -44.80775 | 2026-10-02 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6c5382ae-8261-393d-ad2a-8ff453db1c71 | -5.70222 | -48.08027 | 2026-10-02 11:42:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 22e4e381-1eb7-37f8-805b-d2efaf653179 | -9.08081 | -44.98507 | 2026-10-02 11:42:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 6ea9e0cc-f124-3439-9794-52332cc36537 | -11.7934 | -43.55344 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |


[Clique aqui para ver as próximas entradas](README83.md)
