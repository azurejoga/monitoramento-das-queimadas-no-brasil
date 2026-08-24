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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11910840-4884-3b53-aacc-c7c3fcc20bd0 | -7.3791 | -45.8119 | 2026-08-24 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 74d0a41c-e538-3672-a968-4fe6c44d3148 | -6.3507 | -54.7464 | 2026-08-24 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 455c2c7a-7671-3bd3-bea4-74b301d6b1f5 | -6.8491 | -52.505 | 2026-08-24 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1040c8e9-b78e-31dd-b289-4168b0d3f895 | -17.6621 | -46.3951 | 2026-08-24 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 138.3 |
| ea166b8e-3b88-338d-949c-f1555d480856 | -17.6821 | -46.3908 | 2026-08-24 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 192.9 |
| c631acbf-8b2b-3a89-829f-c83cf42a257b | -10.8174 | -50.9498 | 2026-08-24 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f058dd0a-f424-373c-b0af-38f8edbb37f1 | -6.3316 | -35.1619 | 2026-08-24 00:00:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 471cdaad-c059-3476-834e-88d07a9eaf47 | -5.78 | -57.5605 | 2026-08-24 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 007c2c63-73b8-3562-828d-61cf0c52161e | -9.006 | -65.4 | 2026-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 72030a9c-0fb3-383e-97da-baf013478b45 | -7.3788 | -45.8344 | 2026-08-24 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 27b6e12b-0baa-349f-a4ed-c95f9a8001b5 | -15.4979 | -53.9813 | 2026-08-24 00:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3458a9aa-10b4-33bb-bba0-3ea1fc790935 | -17.6815 | -46.4143 | 2026-08-24 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 476570ae-6588-37ed-b675-64d6d481f3f5 | -6.6048 | -58.3838 | 2026-08-24 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2e67d38b-f3b2-3b42-974c-0202219c7f01 | -8.9875 | -65.4006 | 2026-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a876850b-1c31-3605-b074-f3657501b752 | -9.4058 | -60.5904 | 2026-08-24 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3dd8f3ab-99b7-3479-9b84-6a05f47c4164 | -7.6665 | -63.3261 | 2026-08-24 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| bd5c5e5e-4364-3e8c-9da1-4e06de6d7d29 | -7.7707 | -61.087 | 2026-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 38650047-5745-32d3-9f04-0070210a9b09 | -7.7706 | -61.1061 | 2026-08-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 13d60614-5c6c-3643-9a5b-b6231e762e7d | -8.9876 | -65.3819 | 2026-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0a768128-943b-3561-8cd4-a8f5b9bef293 | -16.3952 | -51.8159 | 2026-08-24 00:00:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 51c6e63a-bfc1-3c57-8c3d-00a7c17220ce | -7.3793 | -45.7894 | 2026-08-24 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 9b94d1a1-8bb0-36eb-98ca-ea2d82bdedf0 | -9.0061 | -65.3813 | 2026-08-24 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 7024cc10-0338-3a4e-b973-4c4ebb9bdfe1 | -6.6233 | -58.383 | 2026-08-24 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7d5d899e-2d61-3682-a6e6-cfa67ba24591 | -16.4148 | -51.8129 | 2026-08-24 00:00:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e0a96565-f74c-3b33-88dc-94b04df7f3c0 | -7.6849 | -63.3443 | 2026-08-24 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3734608c-c30c-384b-9b4e-a18041dd2f23 | -6.1925 | -53.5231 | 2026-08-24 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 43361735-0a4f-3d98-8cc1-5055bcca1998 | -7.3605 | -45.791 | 2026-08-24 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 9993af12-2648-3b15-b970-1ee1f21bdffb | -17.6615 | -46.4185 | 2026-08-24 00:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 8a3b9999-f527-3823-b17f-8bd166334b11 | -7.3603 | -45.8136 | 2026-08-24 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 5e9127ce-137f-3a00-b45e-88c7496d5620 | -7.685 | -63.3255 | 2026-08-24 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 1445f44a-2645-327a-9efa-6bc96088b61c | -6.3505 | -54.7665 | 2026-08-24 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| da8fcc69-73df-3add-962e-9e784766230a | -23.87323 | -52.86168 | 2026-08-24 00:05:00 | TERRA_M-M | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 221e2990-bc49-34ee-95fc-4a642378b29c | -23.82487 | -48.72159 | 2026-08-24 00:05:00 | TERRA_M-M | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8e0dd955-bb21-3934-afe8-ded170754921 | -22.99995 | -49.38253 | 2026-08-24 00:05:00 | TERRA_M-M | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| 4a9a85b8-05da-3dde-a2a8-8205276527f4 | -20.64453 | -45.85282 | 2026-08-24 00:05:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f33b3859-0c16-3746-a4f2-af42a093e726 | -19.97594 | -50.38498 | 2026-08-24 00:05:00 | TERRA_M-M | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 0a73406c-1a89-3904-b21b-b95b6e46cbad | -18.56427 | -44.41031 | 2026-08-24 00:05:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ec35fbcb-2b2d-3f4e-aad5-58e39cc736a3 | -19.98535 | -50.3836 | 2026-08-24 00:05:00 | TERRA_M-M | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 182fcc13-61f6-3a7f-9554-7539bb78f649 | -22.99862 | -49.372 | 2026-08-24 00:05:00 | TERRA_M-M | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.0 |
| f8da060a-c781-3bde-8c54-149addbd9b57 | -21.68631 | -49.68317 | 2026-08-24 00:05:00 | TERRA_M-M | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 805789c6-1c01-31cd-8e32-770f2fb663dd | -19.14772 | -47.68024 | 2026-08-24 00:05:00 | TERRA_M-M | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2427a0b2-749f-3b95-9a4b-012bdc5d9369 | -21.68761 | -49.69364 | 2026-08-24 00:05:00 | TERRA_M-M | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 036ea0ab-f933-3e2e-bbb3-6f77734fb981 | -19.07892 | -47.1324 | 2026-08-24 00:05:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9d8abdd5-b7f1-3b1c-8cde-9499c408b00d | -20.64297 | -45.8424 | 2026-08-24 00:05:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 544ead62-f108-3206-83e6-2e30e7792bce | -20.65215 | -45.84064 | 2026-08-24 00:05:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ec070d2f-0856-37db-bd87-5cd5b3cdc56d | -22.63904 | -47.81251 | 2026-08-24 00:05:00 | TERRA_M-M | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4939608a-e801-3250-870e-fbaf80ced34d | -19.81764 | -43.59171 | 2026-08-24 00:05:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 294fc076-3f73-35f0-a374-301f6fadfcfc | -19.0803 | -47.14196 | 2026-08-24 00:05:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 622ed4ec-0d53-3d4a-9dcc-be89a4a2e835 | -12.10988 | -44.97417 | 2026-08-24 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2735856d-218d-3ae7-85c7-06c4b293bec5 | -17.29358 | -44.87152 | 2026-08-24 00:07:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 47e2f610-383e-3ce0-b001-3e72d4ee0b67 | -17.66938 | -46.39013 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 51.1 |
| c55026cb-5e9c-38fa-b35d-7f9a9fc62879 | -15.0306 | -48.6849 | 2026-08-24 00:07:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 50f3310b-c7d4-3755-be85-511eddd9c764 | -14.94614 | -52.65989 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 78f63c7d-9f1f-3a70-ac2f-f5d83983dc85 | -17.6972 | -46.38551 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5270f42e-cd9f-3ed8-8fb6-0aaeacd13637 | -15.65083 | -56.11225 | 2026-08-24 00:07:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 79038b7f-d3f6-3904-8542-91b34abf6262 | -15.27603 | -52.87152 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ecb01815-590e-3ea4-8bc7-bdf6418ff52e | -11.86257 | -51.68879 | 2026-08-24 00:07:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 757ec118-f30c-34d8-a9e1-549e410814f9 | -12.13679 | -43.40272 | 2026-08-24 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5ce0dda4-34b4-3b66-997b-0023170de5c8 | -15.03186 | -48.69397 | 2026-08-24 00:07:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 01af496d-3b91-3036-9c46-5e30ac0014a0 | -14.98285 | -52.70546 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 51eaae92-c67f-3c4a-b071-9c44a1332cab | -15.75889 | -50.04416 | 2026-08-24 00:07:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 990a28bb-f778-3516-baf2-f4a6b8d4b28f | -17.68018 | -46.39885 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a0c14ea4-7209-36af-97b8-f07389ecce93 | -13.09354 | -43.36436 | 2026-08-24 00:07:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| e644d5ab-1f19-3ffd-80e4-7874052c2d66 | -14.9924 | -52.71094 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 347254b9-057b-3761-9f12-f21b95318278 | -14.94923 | -52.68474 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| af3e8f55-c824-3e49-b97c-2cecd0883085 | -16.06025 | -50.44678 | 2026-08-24 00:07:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3c618761-581c-3978-980e-089c2c5951f2 | -12.60631 | -52.46463 | 2026-08-24 00:07:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bf64918f-1be4-3a24-b6b4-f3f1c71695de | -18.79269 | -50.62046 | 2026-08-24 00:07:00 | TERRA_M-M | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| a2a31736-ffb5-3317-9b30-c39bd04fcfb7 | -16.86741 | -49.45008 | 2026-08-24 00:07:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2cf7f23c-0a3c-375a-9964-3f33200435ab | -16.06933 | -50.44544 | 2026-08-24 00:07:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 2f9925ea-ddde-3827-861b-a54292d7f57e | -14.77619 | -48.77862 | 2026-08-24 00:07:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b3249003-a1f4-3b12-be03-fc4534c38f11 | -16.40195 | -51.82399 | 2026-08-24 00:07:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 144.6 |
| b1abc725-5739-3e1c-8da9-76ad0693bdfd | -16.63229 | -49.35247 | 2026-08-24 00:07:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 86101e85-d9ff-3eba-9b09-502f16ed9916 | -16.05767 | -50.42726 | 2026-08-24 00:07:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8c35d4d4-56a9-3d21-8516-c7c87d65d31d | -12.08665 | -50.60359 | 2026-08-24 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1403b699-d010-304f-8ff1-6b8258c69bfd | -12.08542 | -50.59445 | 2026-08-24 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e5ee5a8f-4ba6-3d7e-918f-a7cee2d8b0bf | -14.97924 | -52.68751 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bec9789c-ad94-3339-ac44-e04ece6fb9be | -15.76784 | -50.0429 | 2026-08-24 00:07:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 32.9 |
| c571a4c0-920a-344f-aacd-92e56c68ebb7 | -11.91345 | -55.8929 | 2026-08-24 00:07:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ea8eec71-34bf-3f6a-9666-95c77be3f893 | -14.94768 | -52.67229 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 9abbd007-c904-38c0-bc50-23f8c17b47f8 | -14.785 | -48.77728 | 2026-08-24 00:07:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 294adc5e-c76f-3a28-a95d-8d66131ddce0 | -15.27453 | -52.85883 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 77a51c0d-44ea-334e-be17-940c006564c7 | -14.35288 | -52.96941 | 2026-08-24 00:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6afca98c-1d23-3aff-944a-2b4d50b632ef | -12.72158 | -48.39968 | 2026-08-24 00:07:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 67aa2fca-507f-3578-bb34-4883f3119f00 | -13.17712 | -51.40639 | 2026-08-24 00:07:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2500932a-9256-38d4-b8a9-79e35531d3a0 | -15.54847 | -47.15206 | 2026-08-24 00:07:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e7539c04-2d22-344f-9a04-3ff7c2eb7554 | -15.26283 | -52.8274 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a4fda1a3-1d66-3612-ba0f-e647012febef | -18.79401 | -50.63107 | 2026-08-24 00:07:00 | TERRA_M-M | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 39.6 |
| fcce88b3-1afb-3739-9629-709da9047b82 | -16.42241 | -49.91468 | 2026-08-24 00:07:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b4eabeae-4ec1-3d86-a779-41cf8e757760 | -15.26768 | -52.86623 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 668eca4d-94b5-32c6-a5f4-66da1175e91a | -14.3974 | -53.0986 | 2026-08-24 00:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e97c497a-bfb3-3edb-b991-964593f37cb4 | -12.60491 | -52.45366 | 2026-08-24 00:07:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c5f95d9e-7d81-32f3-a442-ec54c8326030 | -16.41175 | -51.82268 | 2026-08-24 00:07:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0c002ded-2e9a-3eaa-86bb-7945af60eefa | -16.41312 | -51.83365 | 2026-08-24 00:07:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 51eaed43-c5f3-3a44-b7a7-e765229b50a4 | -11.84668 | -51.71097 | 2026-08-24 00:07:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0155b651-a054-32cb-9f24-3802a6a8c2f5 | -12.07408 | -50.57745 | 2026-08-24 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 60144571-4ee5-385e-ba6d-91f298be0cab | -12.06519 | -50.57871 | 2026-08-24 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1d8cc93a-815e-3a83-b70f-d07d1c5f12b7 | -14.35129 | -52.95667 | 2026-08-24 00:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| e1f09b01-f123-3790-a114-ec0cda877524 | -15.34927 | -52.78387 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 4f0a8b7a-f996-3db3-a977-52bc81eaf0a6 | -14.98073 | -52.69995 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |


[Clique aqui para ver as próximas entradas](README2.md)
