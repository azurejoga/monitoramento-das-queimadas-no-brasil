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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff25251c-f4ad-3d58-8acb-8937818aa6ed | -16.0016 | -50.9456 | 2025-10-08 02:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c94d4ccb-a5c7-35ee-82ce-d3686d266acb | -17.3041 | -42.643 | 2025-10-08 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 431f3215-f5e6-387e-a75d-c17dff2e1a22 | -5.1227 | -44.9682 | 2025-10-08 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 75b1d45c-1d0c-308c-bf2f-88a7097800da | -11.6891 | -50.9619 | 2025-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 41d5f73f-9f17-3225-ab1b-05bb6c4adbfb | -11.1833 | -54.8787 | 2025-10-08 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 231.4 |
| acb7d1c3-68eb-3a27-94b2-9b9fc64b223e | -11.6888 | -50.9833 | 2025-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 59e881b8-23a5-3179-b5a7-c57fab7a64d8 | -17.2847 | -42.623 | 2025-10-08 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 83ff67e7-e5f8-3963-9da3-33aa540a081b | -17.2833 | -42.6727 | 2025-10-08 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6de84f3b-7f5a-37fb-ad81-bff6b129ff79 | -7.5874 | -64.5097 | 2025-10-08 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b47b68ab-8280-3bb5-81b2-453890af9e1f | -7.0167 | -42.8998 | 2025-10-08 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| f66f70df-a0f3-3b42-bc62-c499750b4723 | -4.4978 | -46.3509 | 2025-10-08 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 06b141e5-9d5d-39da-9fe8-873b50bdd39e | -11.1833 | -54.8787 | 2025-10-08 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 218.6 |
| 6b58999e-9257-3403-81be-325598139abd | -11.7082 | -50.9598 | 2025-10-08 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 66668699-d40b-3a71-a8bd-f0be94ab92d0 | -7.7922 | -44.2229 | 2025-10-08 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 0661dfc2-1deb-30bf-b3d8-8234e65e77b2 | -11.1455 | -54.882 | 2025-10-08 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 34d30db5-56d2-3e66-af86-a6ba2bd5c05a | -15.6393 | -52.5688 | 2025-10-08 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9475ca52-4ffa-358c-b845-8692d544230a | -11.1644 | -54.8804 | 2025-10-08 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 185.3 |
| d7faf143-d0ce-350c-bf1e-9891ec665611 | -11.1646 | -54.86 | 2025-10-08 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 3a052273-c9b0-338f-8758-f7ed73dc52d7 | -11.4534 | -50.198 | 2025-10-08 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 59cb0ca8-f198-3d09-b674-35738967fedd | -11.7269 | -50.979 | 2025-10-08 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 1d1f39dd-4969-3b62-bd5d-e0f2dfb8168e | -11.6888 | -50.9833 | 2025-10-08 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 71b41fcf-6177-3417-86e0-225f0899e473 | -11.6891 | -50.9619 | 2025-10-08 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 08f55aa3-d4b7-344a-b81c-f021b3d248d1 | -4.6873 | -45.8504 | 2025-10-08 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c1637312-61b7-35fa-991e-b711b91364a3 | -9.1792 | -47.796 | 2025-10-08 02:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2cc891ed-357f-3065-ad2a-499f7c3284f1 | -11.1642 | -54.9007 | 2025-10-08 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 4f6e33ed-5580-36ce-bd63-7606106ac958 | -11.183 | -54.8991 | 2025-10-08 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 3012cb86-0108-36c6-9dde-79f7a5f1b4f0 | -5.1416 | -44.9443 | 2025-10-08 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3b7590fa-92d0-3dc5-8af8-a334d1403b6f | -17.284 | -42.6479 | 2025-10-08 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 228.3 |
| a3143507-3ea4-3dee-8a41-672482d8788f | -6.9982 | -42.878 | 2025-10-08 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 2081ad02-628e-333f-8e73-55a8e7fe3132 | -19.514 | -44.0768 | 2025-10-08 02:10:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 220d5564-9204-370f-b23d-b15c81695e6f | -4.6875 | -45.828 | 2025-10-08 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 3681531e-3713-3120-aa4f-e8e909b8e7a9 | -17.2847 | -42.623 | 2025-10-08 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 08ee800a-64dd-3ba4-bdbe-2327e3ec90fe | -15.9568 | -42.5876 | 2025-10-08 02:10:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| 5058a568-e7a5-3ab3-9f38-58359e420599 | -7.7924 | -44.1998 | 2025-10-08 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 1146766c-eaef-30dc-b37b-9877885e8f1e | -17.3041 | -42.643 | 2025-10-08 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| c0a7790f-c265-3db1-80c2-787c69738a77 | -5.1414 | -44.967 | 2025-10-08 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| c431758b-fd5d-31ad-b5e6-95c1ada4e5ca | -17.5752 | -40.178 | 2025-10-08 02:10:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 1992d3f2-13e4-3678-aad2-52904335526f | -7.0359 | -42.8744 | 2025-10-08 02:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 0a14e0d1-6f7a-3600-b1e9-6574c8691eae | -5.1227 | -44.9682 | 2025-10-08 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| cf41cc2d-bd00-3b66-bf90-d83f2ae58fc4 | -17.5744 | -40.204 | 2025-10-08 02:10:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 3d3f5de5-da0e-3d99-ad77-2bab5c2014d5 | -14.7184 | -46.0636 | 2025-10-08 02:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ffa79f7c-c56a-3209-b879-c7a23259b795 | -7.017 | -42.8762 | 2025-10-08 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.8 |
| 4948be54-11a1-34a7-a8bf-2650543d66fe | -11.4531 | -50.2195 | 2025-10-08 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 5dee308e-42ec-3c6a-b9e8-193733672185 | -17.2639 | -42.6527 | 2025-10-08 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e10341f1-de84-3bb9-8c21-5a5b9c4e043b | -5.2601 | -44.1368 | 2025-10-08 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7e0df4dc-371c-3832-934f-e92b3c92b56d | -11.7079 | -50.9811 | 2025-10-08 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 351.2 |
| 19c02242-be4a-317e-947f-ee65d3f7076a | -11.1455 | -54.882 | 2025-10-08 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c22b5ab6-70c6-32d3-8de8-0a7d9fa5f55e | -17.284 | -42.6479 | 2025-10-08 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 6f34ac87-9bb0-3963-a37c-c2cb34eac266 | -4.6504 | -43.2038 | 2025-10-08 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 72932917-166c-3955-8c81-0cb7a08a4013 | -17.9421 | -57.5104 | 2025-10-08 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.7 |
| b5d7ec4d-e84d-30e6-9094-64b8711ffbe0 | -7.7922 | -44.2229 | 2025-10-08 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 19c37c03-fefd-3293-a656-f9f94e5d36f5 | -11.6888 | -50.9833 | 2025-10-08 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 50441b4c-265b-3e29-8170-ce266f2b0415 | -11.1644 | -54.8804 | 2025-10-08 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 24305379-8f4c-3bef-915c-7fc95bdc40e2 | -11.1833 | -54.8787 | 2025-10-08 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 297.0 |
| 68b4b2f0-e5a9-3171-abea-a967f3535b54 | -11.183 | -54.8991 | 2025-10-08 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 213.2 |
| 3445e2c1-e9d1-30ac-b6e7-5a8d158b4247 | -5.2601 | -44.1368 | 2025-10-08 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 59dcdce7-067c-3c40-b7d7-3ca39290a504 | -6.9982 | -42.878 | 2025-10-08 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 3e275b4a-d621-338e-aea2-078c95491a26 | -7.0359 | -42.8744 | 2025-10-08 02:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 03d3aa20-cb11-3495-b501-0ecc277c48fb | -17.2847 | -42.623 | 2025-10-08 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d11393e4-6f99-37ad-9c35-7e6dae6b2d8a | -5.1416 | -44.9443 | 2025-10-08 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 64f51a38-2e7f-3b1a-aa45-119faa3af6f5 | -4.4978 | -46.3509 | 2025-10-08 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 1818c02f-62ec-343c-8208-0f449ae2827a | -11.4531 | -50.2195 | 2025-10-08 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c9cc933b-1e0f-3bbf-a736-5d56b65c763f | -7.7924 | -44.1998 | 2025-10-08 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 63276bcb-6218-3627-9c92-e9d050865c33 | -11.6701 | -50.9641 | 2025-10-08 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 82f40e4e-2b31-332b-b4f7-f6ce0da1c0cc | -17.3041 | -42.643 | 2025-10-08 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f3867ee9-ec70-3c35-b466-01d962b4da52 | -11.7079 | -50.9811 | 2025-10-08 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 7d33c4af-ae2d-3c93-9581-82e8d5dddef9 | -19.514 | -44.0768 | 2025-10-08 02:20:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9002c32b-d88f-31d3-a9d6-9396f9ba040d | -7.0167 | -42.8998 | 2025-10-08 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 66f7dcf6-210c-36e0-9e24-5b30b9e02def | -5.1227 | -44.9682 | 2025-10-08 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c98640f5-b4a7-3891-8e75-46bc7759a190 | -11.7082 | -50.9598 | 2025-10-08 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 5a7e8123-2cf3-3d20-95ba-d03b7b399d79 | -7.5874 | -64.5097 | 2025-10-08 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a1d6df79-1ce3-3cf8-a0e9-c05661043ac8 | -11.6891 | -50.9619 | 2025-10-08 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| de549279-4dbe-3673-b28f-5c251b4bebeb | -5.1414 | -44.967 | 2025-10-08 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 80220ffe-8dec-322f-bc97-0e9cae5d18eb | -11.1646 | -54.86 | 2025-10-08 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8d69f4b9-6a50-3f45-a05a-9d25f3f50307 | -11.1642 | -54.9007 | 2025-10-08 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 825059df-990e-3d26-82e8-8817a9682d58 | -7.017 | -42.8762 | 2025-10-08 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.9 |
| ec64b02c-040c-3d0b-b531-6c5022d9f070 | -5.1227 | -44.9682 | 2025-10-08 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2c71e124-2195-3919-b186-8787ab3eb947 | -6.9982 | -42.878 | 2025-10-08 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| b41ceb7e-bb8b-3e19-b36f-00c57a24f43a | -11.7079 | -50.9811 | 2025-10-08 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| db487511-c8e8-31f1-998b-443a687fb8f3 | -19.514 | -44.0768 | 2025-10-08 02:30:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f5b80779-7238-35ad-9c8d-8bad3ee3ad7d | -7.7922 | -44.2229 | 2025-10-08 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 76a5c6fb-88b2-3eb0-8806-de02c4238553 | -11.6888 | -50.9833 | 2025-10-08 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 95d35295-7d71-3684-b54d-35bc02913b42 | -7.0167 | -42.8998 | 2025-10-08 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 3f1971e9-7823-3498-ac8f-1c2351362933 | -17.284 | -42.6479 | 2025-10-08 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 203.7 |
| d7964191-c535-3e6c-920a-4eec95f2f9ba | -4.6875 | -45.828 | 2025-10-08 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 380af5f2-8736-3ac8-87a9-a7712095e452 | -11.6701 | -50.9641 | 2025-10-08 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| dd7b5840-7daa-327f-8853-fe821edf47e6 | -10.93 | -51.0229 | 2025-10-08 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| c68ee11e-8c4a-3eed-9479-2f41c9bd6254 | -17.2847 | -42.623 | 2025-10-08 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ba8e12e3-a525-36f9-bb37-b6d52da30d2a | -4.6873 | -45.8504 | 2025-10-08 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4b3721dd-0708-3716-a29f-361120dbb5cf | -5.1414 | -44.967 | 2025-10-08 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 70abdff2-aeab-3274-98b5-5e5ed8de3089 | -11.6891 | -50.9619 | 2025-10-08 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 0da866b4-5365-34e0-aa2a-777f42a58e37 | -7.017 | -42.8762 | 2025-10-08 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| 8d3e55f0-3e66-3362-8dad-5b7a390822c2 | -11.7269 | -50.979 | 2025-10-08 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 7c933d2c-8fc7-3730-abce-a1a59751faa8 | -7.0359 | -42.8744 | 2025-10-08 02:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 2fd3ad33-5823-34f9-85a8-89ced3f9ea6c | -17.9421 | -57.5104 | 2025-10-08 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 01131701-e3f9-305f-8d02-54d997ac81a0 | -7.5874 | -64.5097 | 2025-10-08 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e95accec-0ca0-3933-a2d4-d21660223c55 | -11.7082 | -50.9598 | 2025-10-08 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| a34a9f50-209f-371f-a1ee-c257e7cf98d8 | -11.7833 | -45.1347 | 2025-10-08 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 896e08a8-cc8a-386d-98d9-8a5869de5abe | -4.4978 | -46.3509 | 2025-10-08 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 1e7c0ea5-a8b6-337c-b426-94b44acb4b46 | -8.226 | -44.2012 | 2025-10-08 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |


[Clique aqui para ver as próximas entradas](README12.md)
