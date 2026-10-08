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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4184fe7e-5817-3d90-88cf-70d18889b133 | -3.01502 | -54.09207 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 7dd67f35-356e-3283-b036-1681f991dd4e | -3.21543 | -53.96204 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9635b371-5078-3d65-8fb4-098231471e38 | -4.53882 | -55.61738 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecec4eb2-f637-3aaf-a99c-4b282260d2b4 | -2.94002 | -54.10832 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63d6e666-aa58-38eb-adac-883cd192c9dd | -3.50479 | -56.91674 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e44cd7ac-52e1-30b3-9215-d60f4b287c88 | -3.31784 | -54.04533 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9489d41d-1c3c-34e5-b5c9-439f65046084 | -3.74042 | -59.47372 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df14ade0-bfd5-384a-a9c4-3d6582718fcd | -4.77138 | -55.73404 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb7853bf-b410-3cba-8d50-aca54d97cc1a | -6.05947 | -59.94248 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dacbca5-c8d7-3215-a98d-cceb74112d66 | -1.10777 | -54.15693 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34e449bf-a0b7-3dba-a6cd-4a6b4bd978d6 | -3.16724 | -54.72883 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee1113e4-7d06-3f78-b005-aa85e6c7d41d | -1.97853 | -56.06372 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58dc3cf9-73f0-31ee-ba1e-3c1a4b2a20ba | -3.29758 | -54.08215 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 278408db-8a91-356c-9ef2-aa271dd5b1fe | -3.32752 | -58.22927 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d89af684-fd0d-3b0e-9b7f-1e502d28815b | -2.7683 | -54.07568 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a430a34-95d3-3c3c-aa6c-c32b4cbd1730 | -4.12292 | -59.88131 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30a43f1a-b9ac-3ee3-a706-c15b5be9535f | -7.22665 | -55.08917 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d8d6284c-6340-3100-9d1c-940a88637bbe | -3.21826 | -53.96551 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42f08eb1-58c3-373e-9d98-13f36cccdc4a | -3.48781 | -54.61728 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 923aa9fa-7d60-3fc5-b5d0-5c4630e7b798 | -2.99458 | -54.08492 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| b0d0b134-1d34-3a6a-927a-c14df3a19a04 | -9.20531 | -66.09084 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05cf94bf-a194-3e95-836c-ef1867ea7321 | -6.2179 | -52.8767 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b5bbcf0-9988-358e-904e-eae2e635af35 | -3.96217 | -56.12293 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f82c5c68-638d-3291-8d39-dbdeb2f38bf7 | -3.41045 | -59.58481 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2d8abef-8cd5-36a3-a1ea-4956f1ecfced | -5.69376 | -53.47472 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4a03e20-a89c-3809-b580-16ae6dce629b | -3.00764 | -57.1697 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e835c6e9-eda4-3656-b5b0-23b1f5ff2eea | -4.37719 | -55.15674 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21f95e0c-9c4c-3fb6-8767-ce635f90b00f | -3.28535 | -54.06828 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d4aaee3-fa95-3567-87e2-69a395fa4595 | -4.78038 | -55.74268 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 244c940e-7d88-37d8-a847-989c1b281398 | -2.99346 | -54.06887 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7fc055b9-2d46-3391-8d83-c38ec1e2ea32 | -3.02682 | -53.94617 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 461af9e6-a91d-3d1b-874f-226849a6177a | -3.02565 | -54.06992 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db9dcc0f-f40f-38a9-ab5c-ae82bbb4c471 | -3.00185 | -54.17682 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fb415d1-bbb0-36a0-a2d2-5e337beefb3f | -6.88327 | -43.70268 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 615a3a2f-3316-3b6a-9ceb-f28f56ee8735 | -4.33666 | -56.38475 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5743882e-7e25-3a4f-b2dd-7d150bfead8b | -3.19581 | -50.55296 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbbb8042-21c2-3dce-a293-c1b96c9d2537 | -6.11371 | -51.73787 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 464a61f8-699f-3572-a484-d127d2dce84b | -4.4218 | -55.75951 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5ccab16-aaf8-3922-a392-c5c15c74cbab | -3.63535 | -59.54496 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c130582-766b-3807-9113-2cdfae984f7e | -6.23319 | -52.8541 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bd498087-4984-3841-9ffa-c5aa50c3a455 | -3.28903 | -54.04489 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79191fdc-39ce-37d9-9cf6-afd36a010c89 | -2.57241 | -56.1569 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdae2dce-a29c-3e0e-aba6-4cabc849b14c | -2.98819 | -54.07615 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5fc59f54-807a-3db2-95b5-e4cea6ddb962 | -6.30342 | -54.79164 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7be1b39-06ea-3eb8-88e3-6f2b8f4b9214 | -3.18101 | -58.64301 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2711a00-1c9e-32a7-9cfa-d998cef7826c | -3.63177 | -59.54438 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e67a1ed-6fd7-3e94-9621-7ef3db6213d2 | -3.54085 | -59.41456 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ec4ddbc-5db8-3945-9b82-119328dd79df | -4.74943 | -55.6541 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7db8fe2-031b-371c-ae99-cc3663d82fd1 | -3.56733 | -54.49466 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e95cb8-0a6e-312b-925e-a20d08922cc6 | -3.23803 | -56.82525 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee8fdecc-f465-38bf-acf8-91e0abc2214b | -3.07998 | -54.18405 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d0e6cad-3454-399f-9258-c6209ce8b4f1 | -5.1123 | -47.12555 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ba88f36-c3e0-362b-9f60-e48a03e5509b | -2.94189 | -55.78838 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04d0df0c-4aec-37f0-b3cf-31d2b92be191 | -3.01542 | -54.13566 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c89af21-d722-325c-b6b7-b222e73302a5 | -4.63166 | -48.85769 | 2026-10-08 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89cb4952-c9a7-3f1c-be85-485ca23bb58a | -4.11006 | -54.02252 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4286c0bb-24e4-32ac-9ff0-77a5c1a0b31a | -3.30727 | -54.04368 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb570d75-3e58-3d29-8364-6b235eed78b2 | -3.09053 | -53.93194 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0321820f-f3a6-355d-9718-f5d81ece1856 | -3.39067 | -56.9307 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1408a99-7c8a-3748-95c7-54303cf2e29d | -3.01442 | -54.09594 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| d8b44395-5ca7-3c98-83b6-6e72ab860775 | -3.03497 | -54.07928 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d48d0c4-2d0f-3fca-a09a-4db69da32baa | -3.94437 | -55.71436 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6bffd04-ab2d-316f-9bd7-866f942fc22c | -4.12085 | -53.80907 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28292dc9-c99a-374c-8eb8-e132ec2ba87f | -3.98035 | -56.2184 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c4b129a0-fcc4-3ffb-a576-54d6efe6f85b | -4.07282 | -59.84516 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79b730fa-bdf7-3a37-beb8-486c6c208d01 | -9.47794 | -64.36592 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 890847c3-1440-3b16-b246-757f49d05608 | -3.48012 | -59.58762 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16d06976-9069-3608-9dc5-3c4f297940bf | -6.7321 | -55.12275 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27b4026f-ff8a-3f5e-915a-23304c08cac2 | -3.97554 | -59.33361 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be9fe6e3-c773-3c48-bb5a-ef9da66ca765 | -2.5086 | -56.17894 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11044047-d0d9-3938-a0ea-8f3f9e335552 | -7.20257 | -55.12929 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba811d61-8f60-34bf-b6b9-adf600efaa9c | -4.09325 | -52.06278 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1522f196-9011-3d3a-8cfd-b558a5b3332a | -2.57797 | -56.16485 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c96b3dfa-0e6c-3b70-ab10-7bc53d3f294b | -6.11719 | -55.69735 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a51a534-b8f6-344e-bb51-9ecb25d903a4 | -3.34876 | -54.16824 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b787d28-0439-31fb-a240-e1bd648524eb | -2.50469 | -56.16062 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a7a987ff-f952-330d-af2c-003dd01de7d8 | -3.28765 | -54.07661 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d215d0d3-279c-3d91-bac3-766b9e78a450 | -2.58129 | -56.16537 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72e68ce7-040b-37d5-a627-4e52fbac3fd6 | -3.8763 | -55.99512 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a65f293-3e24-38cf-9c74-6d24fac60cf0 | -2.76921 | -54.07495 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf2034ca-eeef-3e80-b93f-7fc5d0bb3777 | -2.78151 | -54.06499 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a05fd3ec-f51d-38a1-9594-16430d2eea3f | -3.53784 | -55.52455 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a419b1f4-36da-3afd-8f9e-2fe4c2899920 | -5.07239 | -56.90588 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b246fbe5-604d-3c9a-b187-1c159bf7210e | -1.52503 | -54.5169 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaa0dc78-624a-3999-a5ed-8cf048ba620a | -6.71413 | -55.04614 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9915402-91c0-3070-b651-55bdc912f031 | -2.48638 | -56.14713 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3c81682-6ee9-3b45-ae46-96a85b71e9b4 | -4.11882 | -59.88244 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6cfaf2c-20fa-39a8-8aae-da9524c5a234 | -3.02159 | -54.18788 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8279ea54-8d1b-3a11-b5b4-c5278d942f14 | -1.52597 | -54.82029 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e6a9402-cafd-33e9-8d9a-d05208502b14 | -3.01552 | -51.01662 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c6d9d37-da2f-365f-bc2f-76b00df62b9f | -3.75809 | -59.46699 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b365ab32-e7e0-3ed8-bdf1-b0b3009b4638 | -4.27315 | -55.71111 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff40dfc8-c1a2-37b3-a1ca-d5e756bee0ca | -3.55242 | -50.09556 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f60f3f7e-50da-34a6-86ec-fb1cfdfd0d5a | -2.76297 | -54.08669 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4b2c223-6682-36ed-a423-1eb5a5f627f9 | -1.44152 | -52.85335 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aea1219f-436f-3ad9-ab75-08a80168d63d | -2.63074 | -56.6233 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13d246c4-f404-3493-91d1-0fc8ca07b76a | -3.34715 | -50.47567 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d7131c97-9eef-303b-9f4b-a32212ec2105 | -3.05812 | -53.93095 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 350e195e-9c78-367b-93b4-08e531e4805b | -3.02735 | -54.08208 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21b76fed-d360-342d-8abb-7bcc57094917 | -3.30623 | -54.02744 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README154.md)
