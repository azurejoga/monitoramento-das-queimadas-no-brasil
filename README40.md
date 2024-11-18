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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fc74bf6-e746-39ce-a31d-bb69c53756ce | -1.29076 | -51.7378 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac118275-41d5-37e6-a57b-2fe2a529f190 | -1.3197 | -51.87096 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1aa9d99-9af2-3b60-8cf7-396e36e6f544 | -1.62195 | -52.62638 | 2024-11-18 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7877008-503d-36f5-96ca-e8d3cac6fb58 | -1.63283 | -52.58892 | 2024-11-18 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b88707a-05fd-3644-a67b-674f1ec3fbc0 | 1.05825 | -60.60489 | 2024-11-18 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1187e311-16d7-3a25-ab26-57227ef7126b | -1.41713 | -52.42677 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec089b53-24ec-3e42-95c4-d7e4165f738d | -1.20688 | -51.76942 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aaa550a-6888-3216-a6c6-91f9a7d45763 | -1.30096 | -51.74286 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 65c7dd52-b48f-3496-951b-ec35ffdb5864 | -1.41201 | -52.42597 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3387b85-7d7c-36eb-9329-4feee40eb803 | -1.29126 | -51.73445 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 771ca499-0f38-3ccd-a6c0-9615e3fa13c5 | 3.97168 | -59.69737 | 2024-11-18 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cceddc54-f52c-3d74-8e2b-aba80041229d | 0.79769 | -50.22462 | 2024-11-18 05:27:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd37c7b9-0bec-39e7-9da0-cddb1d081dba | -1.27449 | -54.66909 | 2024-11-18 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49006772-6a23-336c-8694-9e318265198c | -1.20536 | -51.77943 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e75f1631-a7b2-3f1c-b47a-68499c1ace4b | 0.61299 | -51.77069 | 2024-11-18 05:27:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8d16491-9cd1-37cf-941a-999f3e2b9c7c | -1.2107 | -51.78021 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e963aa71-11cd-3659-9a14-691d81491a0b | -1.72878 | -53.26965 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9bc1e82-9a7d-34cb-bbe8-c6af86ac6240 | -1.30392 | -51.7436 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| feaebcd4-9745-3aad-8c71-a13f371df4f9 | 0.79704 | -50.22071 | 2024-11-18 05:27:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84aa1acb-3826-3afa-8b66-d559a3da3bca | 0.61866 | -51.77298 | 2024-11-18 05:27:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8c173e08-3592-3dd6-a622-d43641578a3e | -1.63423 | -53.28587 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b7b081e-5025-315e-bd4d-3af2ebb0c808 | -0.1583 | -51.59811 | 2024-11-18 05:27:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aae968ff-3a8f-393c-8d37-b07ca647822d | -1.18412 | -55.73221 | 2024-11-18 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85e43cea-f38d-39e2-bdf6-19393c794043 | -1.30498 | -51.73689 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0e4e07c4-1c7e-3ceb-b4d4-3360ff15df62 | -1.62699 | -53.30093 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f71c904-0373-3d7a-8516-357c2cc5823b | -1.77052 | -50.74662 | 2024-11-18 05:27:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e01662eb-1864-3c11-ae0e-f0cf22002d4b | -1.63183 | -53.30162 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3da3d3b5-752c-328c-8638-658f22ce6c15 | -1.30016 | -51.7327 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08fd279a-0f96-3f41-a9c4-e6cd30ff6212 | -1.62239 | -52.62344 | 2024-11-18 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c5a67a0-1277-362c-980d-34bb4f0c0823 | -1.2747 | -54.66712 | 2024-11-18 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c1cd0a7-ac4c-3984-b0fb-ab7d02e63802 | -2.16965 | -50.60873 | 2024-11-18 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 670b19f2-d585-3e8c-895c-1d5818538059 | -0.1631 | -51.60225 | 2024-11-18 05:27:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15b67ab6-097d-3af8-a03d-cf699166092c | -1.63836 | -52.58675 | 2024-11-18 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3590dc5d-2065-3ddd-9645-d9151e24fa9f | 0.61817 | -51.76982 | 2024-11-18 05:27:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a0d003ac-e412-3f16-a0db-16d9bae59ea6 | -1.39283 | -51.98854 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 204d08be-a4bb-36f1-b352-b34ed65f2cf3 | -1.20638 | -51.77276 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14adc80a-b68d-37b9-9e09-f9fd1268b2aa | -1.32019 | -51.86774 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d6034b2-3833-362c-b919-e7269d363ac0 | -1.77111 | -50.74266 | 2024-11-18 05:27:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f0b135b-2281-3cef-8f53-70f5d8f4781c | -1.67616 | -53.83793 | 2024-11-18 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8186c561-b739-3280-94d8-2b66e1f6cabd | -1.43455 | -53.38102 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 17463d8b-3fef-336f-8d5c-316f78631ce4 | -1.43935 | -53.3817 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2554104d-0314-371d-860f-21812df1c7ac | -0.16361 | -51.599 | 2024-11-18 05:27:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59afa0b5-a2ac-3325-80d9-5d05d993ba38 | -1.30631 | -51.7437 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d83ad9e1-ddb3-3ab1-9410-477d3f39ee4e | -3.77313 | -50.16647 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17227fd5-071f-34e9-9172-439c658ce606 | -3.30502 | -53.36871 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8f61410-ccc7-323e-8216-19c6ed46fd03 | -3.6949 | -50.11122 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d06f754-8a77-3cad-a04e-313b466cdeeb | -3.38811 | -53.26305 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cab14114-17de-34db-8a51-4ae965bcca37 | -3.50513 | -54.03742 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b8d5ee3-28bf-38d2-92d6-93142329ae85 | -3.52285 | -50.2553 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87f962ec-e0a3-3180-9c68-5d4b20608e15 | -4.10677 | -51.05935 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8e63f19-368b-330d-9bfa-7569309aaf41 | -12.55524 | -57.81572 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdd36a77-af1f-361e-afbc-bf9b64f8b31f | -3.56042 | -50.25806 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b23fe8eb-f565-3646-8db1-36a041f93027 | -2.23403 | -53.60639 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c20c9581-922d-30df-8d51-f95a49f3791a | -2.37353 | -53.68125 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c077a68-b803-33aa-a243-e303fe3142a3 | -3.13983 | -52.98167 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db4d485b-8652-3a16-980f-ef4e8093ba4a | -3.5808 | -53.27021 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fe751e7-4a88-383e-b6d9-39487ce4e061 | -13.01797 | -56.45223 | 2024-11-18 05:29:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c541812-c860-3ee8-bfeb-65d480079cb2 | -3.76762 | -50.16102 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f1f2f8-5369-3418-8e33-f5a590dc8479 | -2.59138 | -51.71622 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a784cd9-70e8-300a-a6a9-2312980d4fe7 | -3.1905 | -53.25302 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6755a82-dad9-370f-b106-5ad8f8fafafa | -3.14028 | -52.97871 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f9843d9-bfdc-3f08-8764-08c965bcfc68 | -3.76752 | -50.16423 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e97013ec-4975-3676-aee6-e3e278ddb560 | -3.47562 | -49.97497 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d21cde9d-d6b8-3be6-adf4-503c15a074d8 | -3.06105 | -48.00009 | 2024-11-18 05:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f95904d5-4dae-3f61-aa83-894aa9ace34f | -2.33103 | -53.57501 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f08b636b-38ec-3590-89bf-447736ab3439 | -3.04304 | -54.40219 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b597b865-5345-30ac-b460-5c71daacd822 | -3.02714 | -54.10405 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53fb2a2c-b8c6-39c2-bebc-ff68b3a875e0 | -2.36878 | -53.68049 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e91dd64f-c51f-3af5-851b-f83e8644eaa2 | -3.53026 | -50.24741 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebfb30a7-d0e2-3ea6-b1b2-608b22a2a23f | -2.2388 | -53.60713 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25237f3f-c1e3-3b4e-bb99-d910515b5012 | -3.3121 | -53.36505 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91c3ad32-9762-3cb7-bca8-b46dbf3587bf | -3.04761 | -54.40287 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a10bff0-b2d6-3d23-beb4-7f0728d6dcfa | -3.19137 | -53.24727 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4c316ee-4e5f-3475-a702-8e0bb2bc7989 | -3.04206 | -54.40497 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4921381-8ab3-396b-aa20-e381f6212678 | -3.76695 | -50.16571 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b61fcc2-b777-3857-8bdf-7a29997ac053 | -2.58482 | -51.72243 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f971b39-e6b9-3964-8d89-42c5f01c74a2 | -3.04231 | -54.40683 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0df6a1b-f9ef-3f59-8e17-b39ccc54eab5 | -3.33432 | -53.35139 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 224a61af-6d3c-309c-852b-f418baa0684c | -3.57497 | -53.27505 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e6ab835-9514-3e9f-afb2-ffd45f35f8b6 | -3.74299 | -54.71926 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 246cad8a-d16a-3745-8770-43fe9b5305a9 | -3.58096 | -53.72119 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39c87193-7318-3f7c-adb3-44a58e29eff7 | -3.0512 | -54.40649 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 04e149f3-95a6-35fc-8336-d4c9c40618c1 | -1.77594 | -55.53355 | 2024-11-18 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe916c66-8b60-3454-ba68-33a25593a7ce | -4.10036 | -51.06239 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 020eca9a-7a9b-3c72-9931-33b3922f79e2 | -4.10619 | -51.06337 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c827e3d-6e65-3e7f-9f74-23b4f0609275 | -2.13367 | -52.07155 | 2024-11-18 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca39a004-3093-3289-a254-30edec643e84 | -3.57785 | -53.11625 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ff52502-919c-3f99-96ae-c058ce0640c5 | -3.56722 | -50.25412 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4356e475-525b-36ee-aef8-f25df44cc7df | -3.04689 | -54.40755 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 365a673a-cf7c-37a2-ad69-27a7e50af445 | -4.274 | -50.58791 | 2024-11-18 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27c588c1-9934-35c8-b5c8-49d4f16b53e3 | -3.04274 | -54.40034 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 127171fa-a9ca-33b8-ab67-80d1ab19d74e | -3.05647 | -54.40249 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a8729e13-65b3-3f5c-a20b-46ae867d4997 | -4.06404 | -54.05087 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f82a571-847e-3b97-9653-1634c78138fe | -3.52487 | -50.24173 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1100769-6bf4-3f02-97cb-c14a369a9986 | -1.72683 | -55.0183 | 2024-11-18 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21d4cdb6-b134-39f3-995b-a2995f9063b5 | -3.30633 | -53.36994 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 958e084a-c587-3d65-8018-5558ab2b23bc | -3.52995 | -50.25323 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dbc6939-1ce2-3253-acf0-2be98c00fee0 | -3.62758 | -50.22571 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 739a6249-34b0-34e3-a521-8eba179e9483 | -3.14402 | -52.97977 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb147d00-d870-37a2-8356-f9eb3fe06b34 | -1.80454 | -54.03178 | 2024-11-18 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
