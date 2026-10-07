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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 540e5553-7571-3af4-a358-8c652db894b7 | -2.78508 | -57.65332 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80610e6d-4a4d-3511-bee7-16e6db2e7ca1 | -3.52468 | -58.75898 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36533589-5cc6-342b-9f29-524e48d83beb | -7.19003 | -52.62624 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49fd3051-f24e-32e0-a92c-4fe7257c7752 | -3.09606 | -54.28151 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a8057c9-a727-3a1a-b491-3bfcd50cebba | -2.77003 | -54.08045 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c203b0c8-a715-3709-a146-10ba2953963c | -3.23106 | -53.89111 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44f21fff-442a-3a75-954d-0b252cdf3707 | -4.09913 | -52.06824 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc84b23d-08a6-3598-a196-9f536bcbab41 | -3.09546 | -53.7164 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3410e38d-8218-3038-86e9-a2b5c1b74149 | -4.56472 | -55.05721 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4862d277-d486-3d62-a38e-c7764e39c7d4 | -3.71592 | -59.68921 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f43bb0a-386c-3419-b7d0-96ee4078821e | -3.55549 | -54.69809 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1101faaf-fdfc-3b24-b139-825d7c22c093 | -2.99875 | -54.11949 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b879e706-3fb9-33fe-a3a9-883ce57582c9 | -3.85468 | -55.9842 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80d16468-46f3-3f09-bdef-9a9886cdfa5f | -2.93414 | -53.94373 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afa0eef6-97b1-38b7-a9f3-a79d0a58aaa4 | -3.32767 | -54.19177 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 031cfddd-e6c4-38bd-b71b-d3b1d59cbcf4 | -3.54259 | -54.65002 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bf6e0f54-046b-3f30-9e96-ed4aa1f6f000 | -3.48217 | -55.42924 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e7cdbdb-d5e2-3f5f-adca-c84431f8594f | -6.92239 | -43.66297 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| ae0ee21e-da9f-339c-b434-70733ffd9887 | -6.4082 | -52.72095 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49272ad8-acaf-3ee1-af44-dd6744905494 | -2.96054 | -54.14592 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffabe0e5-2bc3-37cd-93ba-7642f2f0c528 | -5.2402 | -50.91922 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a943b866-ae85-30cf-ad80-2fe709a47553 | -3.07819 | -54.24298 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 633bd050-4008-3b3f-b669-aa32382ef825 | -3.50842 | -54.62716 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 263895ee-4c0e-3c9f-b32f-12286c110d64 | -3.10281 | -53.75792 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb1f770e-741b-3303-aec9-7e0804312204 | -3.27047 | -54.01356 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2a43bd4-56a1-3541-93b9-bcc726bfda98 | -3.85412 | -55.81472 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cef9c3cc-aee1-350b-a377-9a4acc71bf6f | -2.98183 | -54.05204 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abfb117d-8359-3dfe-b161-fb1e22d307a7 | -3.0918 | -57.6445 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b5ca5cd-86f1-3893-a996-5ba2914eb737 | -2.88475 | -54.15239 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8e623a4-bc4f-380f-97e4-98df8c58e8ad | -2.98045 | -54.12743 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5aed04e-57b0-31d9-808e-6dbab0ab7928 | -1.20084 | -54.21424 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8250af4e-177d-3497-ac7f-e22eef1bfda1 | -4.11829 | -50.82497 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77d83ced-242f-3ccb-9bf3-9dc79a078ff3 | -3.2758 | -50.03648 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e03d5a2-205c-34c4-a3c0-1c4493403f0f | -3.86183 | -55.98177 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6adfdfe4-8345-32ee-9d6f-6d1928b5dcda | -6.00498 | -53.50127 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67c9550e-8f95-35c5-98f1-4264bb0fa700 | -3.07461 | -54.17788 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9150407a-857c-36f1-a495-97a2334f9bc9 | -2.56479 | -50.68484 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f443511-c58d-3dd8-82f8-86f8db728a91 | -2.95397 | -54.16645 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 720940ce-a123-3e8c-aada-ff0b1535c45e | -2.99032 | -51.04438 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b6994bf-1b28-3abf-97f2-e19e2d357857 | -3.2663 | -54.25787 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fbf4491-4e15-3899-9fd3-5b6806a5cdfd | -2.01689 | -56.89193 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5724865f-463d-3dc0-9834-731de03dd372 | -1.61565 | -55.11503 | 2026-10-07 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f491e6c5-38b4-3051-a5f9-7bb5f9b9c85c | -5.95435 | -55.3523 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84073970-6724-323a-9091-43095251a244 | -2.75181 | -49.53603 | 2026-10-07 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4395413e-8cfb-3dd6-9a52-e363e9b5fa0f | -3.0285 | -54.23531 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6092443a-3c94-3310-928c-c5e2195076c5 | -3.36096 | -50.76269 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a0356cf-6b64-3cd4-bd3b-c4c518e9920a | -2.80391 | -54.08206 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e327375a-512c-3844-b474-f5a2e4291b71 | -2.63727 | -57.71843 | 2026-10-07 05:04:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a466f47b-a427-3020-80e1-4e591666b995 | -3.09793 | -54.18148 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a83996df-39f5-3854-a2f2-35960a8a2438 | -2.96171 | -54.16047 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 143d78ae-5d0f-3dd5-bcc6-fe2bfdf722c9 | -4.26443 | -54.86522 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f436e5-0185-30be-bccd-7228cc29e5a3 | -3.01099 | -54.12857 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c124698-5384-3251-a616-7c0335048109 | -2.89948 | -54.07926 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b81f0d43-00c1-3ea4-bfc9-4a6f5b053a1b | -3.20693 | -53.8762 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72983a5b-9327-367a-8164-1062d33b0f68 | -4.24814 | -50.73242 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ff9671a-3d8b-34ec-99e1-32f8cfe5cb3a | -3.10676 | -54.16845 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26f1c2ef-6ec7-3fac-ae0d-e3dc77ce9b40 | -3.07944 | -54.27894 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 283bafb2-5676-3135-b301-7b502f7d3ed6 | -3.32275 | -53.85406 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85bdeea9-6a3e-3ca0-8401-22f1677c6c31 | -3.2114 | -53.86957 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f0c507d-8abf-39b0-af57-67a95955f7d2 | -4.03816 | -50.98425 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fd198fc-ccbf-33a0-962e-66233eae2586 | -3.67662 | -55.94963 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f25bcdb-3946-330b-b72e-05d6ab462431 | -4.91911 | -55.85986 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c12728da-f866-3e26-8d48-ac435cd555e2 | -3.39173 | -54.17261 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 662aefaa-b084-37af-90c9-5688a1b3a2ce | -3.70935 | -59.67112 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df7a106b-6795-3a01-8a3f-c1c99ab07f34 | -3.27051 | -54.03531 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8ca0218c-c515-3153-8639-8436c08b63b8 | -3.275 | -54.05048 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4f794fa0-3ad4-3e68-80dd-6c7dac1a1b72 | -3.0501 | -54.22789 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02f633aa-b014-35f9-9aff-f4655f0940ea | -3.28775 | -54.01258 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5276707e-0543-3c3b-a302-5c64f1400779 | -3.35706 | -50.76208 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9050e4e6-e5c9-343e-8011-9f3ff73c6361 | -2.86439 | -54.1959 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1a83f28-2a65-3cbd-b63d-f377fcf8fde1 | -2.86251 | -54.14183 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab5f2170-6eaa-33d8-83f9-79897505ba5e | -7.29723 | -47.26012 | 2026-10-07 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d12539c-3ba3-3134-901d-515f7c7a1db3 | -3.42466 | -52.549 | 2026-10-07 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ceac453-6637-3017-b3cf-d3ea67d38e6d | -3.72499 | -54.21694 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64f788e5-638c-37ba-8d18-d8405247178f | -3.07208 | -54.23846 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cde40c2a-c05b-3726-8077-e703609ec3a6 | -4.27051 | -54.86973 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a45b0b7-6b92-37e0-9fa4-43c4a56e8320 | -2.94354 | -54.14712 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c24bae4f-745b-35ae-be76-d0369ac065f2 | -4.13197 | -54.90491 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d138cdaa-15ba-326a-88ba-5dc62793234c | -3.28224 | -54.04797 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 930dea65-074f-3c5c-b1ba-540cdd6592f6 | -3.38389 | -59.43036 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b64a638-6b25-37b0-b7af-9012a4ac66d8 | -3.6893 | -55.95512 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2024e1fc-134b-3130-80f6-dc47a41ac2ea | -3.0433 | -53.94213 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83cd69e2-314c-3751-900a-8be4ebc99c1f | -4.15129 | -55.15476 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b105d88-d204-3773-a1f9-ba911d3cec11 | -3.54279 | -59.47968 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb674c4-68c4-3731-ad79-facb039eb427 | -2.89032 | -54.16045 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf7f745b-50db-3af8-a42b-0762c87e4c20 | -3.16625 | -58.63219 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73aca503-4fbe-3692-b06b-85290da84517 | -3.06324 | -54.14378 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19beef02-37cc-3b44-90b7-41988ae7cee6 | -3.99167 | -56.26168 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2fdcd225-71e8-33b8-8470-33347160e55e | -2.88196 | -54.1484 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b736a372-1d95-3cff-92ad-313a7b25ca47 | -3.07182 | -54.17385 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98d7c285-540b-3030-8e50-9736ed0fb97a | -4.90113 | -54.99281 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29cb3a69-c7fb-3265-b14c-17f2db6caa29 | -3.52011 | -54.66089 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e15aad1d-f8e0-3c94-bacc-1374b2fedbec | -2.5747 | -57.78915 | 2026-10-07 05:04:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34e98055-0f21-3b39-b3e5-6cd6fec5c79f | -3.28106 | -54.01156 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3dced869-867a-3a09-b19e-8e6ab1de835b | -3.06344 | -54.16178 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f97aad30-6b01-3e93-870f-16fbea9d04f4 | -3.07495 | -54.26394 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bbbe0f7-1449-3ee4-986f-337eb78bd5ca | -3.09324 | -53.73076 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ee6e4f0-8723-3d1f-95c2-f7371b99e275 | -3.29007 | -54.06364 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30bb22b2-d8b0-3e79-be7e-490e419e0207 | -3.09884 | -54.28551 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3a64cfcb-6565-33c0-b4fa-9b93adbf112c | -2.90901 | -54.10589 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README91.md)
