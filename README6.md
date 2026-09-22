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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdf65b99-019e-3ce4-9c95-5a8e313940e8 | -18.718399 | -46.938202 | 2026-09-22 00:57:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b59da26b-3b24-3524-9987-359473902d48 | -3.0444 | -54.400799 | 2026-09-22 00:57:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4fccca5-d700-3e9a-9db8-a98b12124723 | -6.9134 | -59.6278 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bde55ba-758c-34f9-b3db-abf7734a39a6 | -21.4436 | -48.675598 | 2026-09-22 00:57:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6781e798-fe59-36d0-9b70-7eb539c7beb7 | -3.3933 | -61.052601 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c49fbda-3d37-3569-b880-6b756fc693e6 | -3.4765 | -59.567299 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8e54d9b-41e3-335b-a54e-290cbdfe26d7 | -3.0695 | -61.169998 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8f766f-184e-30dd-b874-c036050ff0d0 | -3.3565 | -61.298302 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08ed267c-3574-39a9-be7c-f20256c303c1 | -12.792 | -54.049801 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3da07451-3c30-386c-90e7-61d669ed2b0c | -6.6164 | -59.905998 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 664c71af-bab9-390d-957c-5157e2ba2ce0 | -7.5721 | -57.666801 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d09c298-17aa-38f1-bca1-bb0e0497a24e | -6.4254 | -59.972801 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea84bbd7-e2e8-3df0-95e6-a0aa0abef06b | -3.4576 | -58.322399 | 2026-09-22 00:57:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0522389-79ca-3c1e-a26e-e2fff5206e86 | -6.0758 | -57.618599 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7301adfd-92d0-3a97-a894-6cac564e5cb8 | -10.2232 | -59.397202 | 2026-09-22 00:57:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89c8df9d-502c-345e-a81a-4ae72e99f9be | -7.316 | -55.589699 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa24b39-9ed0-3789-855f-871c6c1a6a5f | -3.7874 | -60.746101 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eed7ae46-9b62-3bbb-a46c-406a3a0fbec5 | -8.6207 | -54.635399 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dbc2811-650d-3753-94b1-cd93d5c708b1 | -6.4271 | -59.980099 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6847c7d7-13c8-3215-86da-94cf4ab168c7 | -8.2399 | -55.274502 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349da0c4-53f4-3861-9d27-ce96421a673b | -3.0793 | -61.167801 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53faff04-31e5-3c88-af40-aca7e3c299d3 | -6.1324 | -59.954601 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f32f2cba-d86b-3e71-a5ad-6d782bd60aec | -4.257 | -60.0042 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13a1d506-4f3b-3515-be48-4de39ccb31b0 | -3.7857 | -60.738899 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21d864d0-edb6-36fe-89c1-70b76a5bd2c8 | -8.2467 | -55.2598 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68edfaf0-b99a-3856-b6a2-f3da2729f704 | -11.7602 | -50.8214 | 2026-09-22 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 595b0e46-cef1-3d03-98ef-c4f8691bfc4c | -12.7857 | -54.024399 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af234c9b-18a3-33ce-8d61-62f17df2122e | -6.0989 | -57.672798 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac7205e0-80aa-3523-bdd2-b661c4babfbd | -6.3501 | -59.959099 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1995577b-5c2c-3cf8-9179-4b6ebbe7cc92 | -9.2978 | -58.9175 | 2026-09-22 00:57:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef7d46b-9a97-354b-822b-4f97509bd5f8 | -3.3913 | -59.510399 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30f4a2eb-e1c4-3bbf-b508-2fe76bfc2ff2 | -3.6874 | -60.624001 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2feba059-7cc0-3bc0-9b38-40b21fc3d726 | 1.5474 | -55.915199 | 2026-09-22 00:57:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24df6315-b53a-3e1b-8a90-c99afb4caff4 | -6.6903 | -59.958401 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5ee22c0-becf-34bd-8065-fcf3dcee1074 | -6.6376 | -59.908901 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 558ce9be-81ff-31ff-a599-951a69235627 | -6.7419 | -59.063 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f24b3e1-30d5-3eb4-84ef-899874f6ae3b | -6.721 | -55.085701 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a336a7b-4793-3067-bdfc-58c8b710f4ff | -3.4783 | -59.575401 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed7392e8-60de-35fd-ab16-7f86215181be | -2.925 | -57.800098 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11df9644-cdfa-3e70-840c-a0af408d67a6 | -9.562 | -65.987602 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa7e5c24-73ae-36aa-a6df-e1ef0c610f31 | -6.0597 | -57.858101 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40bd8d34-fe94-3e71-8643-9e5b054890ea | -3.326 | -59.810001 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b91c72b4-6ad0-3712-b605-86e6fcb8e803 | -3.7759 | -60.7411 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3709ef4-bedb-354e-a878-5913ed1af895 | -2.4162 | -58.2705 | 2026-09-22 00:57:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e81c49f7-2f44-3f0a-950a-fae04df87691 | -6.6984 | -59.948898 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb7f4ee-c6f4-31b9-ab03-cdf583709a22 | -3.0633 | -61.0518 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72c11b07-6bc7-3aa2-a401-772a925653b6 | -3.1006 | -60.717701 | 2026-09-22 00:57:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28652262-b669-339b-9571-b9033460b24e | -4.2049 | -59.912102 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48ee9697-5a9f-3a63-bbfb-7a2b2fae39e3 | -6.1564 | -57.698898 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff1d10a-f841-37a9-9149-c2afd695d7be | -10.9286 | -58.339298 | 2026-09-22 00:57:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1afa0d89-1897-3c8a-bcb3-323ca8a67971 | -7.5819 | -57.664501 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5730c35e-a9c1-3a81-81db-d499857c7b55 | -6.3078 | -59.999599 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53f7838e-757c-377b-a63f-d09df5274dc3 | -6.7001 | -59.9562 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ceafcc4-33c7-3ac6-a114-64be90a7c416 | -6.6295 | -59.9184 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63907319-f002-366e-9f1b-505b0eaf01ed | -7.2904 | -59.5177 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68ba7d54-83d9-3125-8873-8bb933383c5e | -2.9227 | -57.790001 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92df71bb-5b68-313c-8857-8415350cce0c | -3.4185 | -61.299099 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1bc63e-6d9a-305c-988c-243a68ce4239 | -6.2927 | -59.933601 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0ea0be-e9b2-3d2f-8218-96495d7e22ff | -3.243 | -60.800201 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07bde36d-05e8-3dd1-a3ed-092d51455fe8 | -6.3848 | -60.020599 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c79fc52-3a67-3fcf-aa60-dc95d145e9e5 | -3.7518 | -59.4202 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1aa057-e9a3-3754-a7d0-c0602f2a84e8 | -10.2037 | -53.901501 | 2026-09-22 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 173edbdf-6097-3c97-8dda-d122e9cb6c4e | 0.7908 | -59.181599 | 2026-09-22 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac51bcd-0e1e-34e0-9355-372b2a198d52 | -2.7827 | -59.957401 | 2026-09-22 00:57:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea87a262-91c4-31db-9981-138c25487175 | -3.1906 | -60.434399 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e95e22f9-a998-3ecc-895b-ca998954df3d | -3.0748 | -61.056801 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2439c774-2049-3a19-a687-9a81e76c8454 | -6.2912 | -57.7458 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e67b36-5d45-314f-84b6-de0915745a80 | -10.8599 | -57.164101 | 2026-09-22 00:57:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2abf733c-57e1-381a-8e6e-f33c844f6f37 | -7.3938 | -55.227699 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0d81b2-b513-31fd-98f9-e4dcde0fa167 | -10.5984 | -53.994701 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4e3e08f-6cc3-3263-b6bc-afe52912058f | -10.4591 | -51.286201 | 2026-09-22 00:57:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69a88dd0-9d95-3fa8-b6fe-b08299da08ce | -6.3555 | -58.286098 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bbe2dbd-f54f-3cfe-979e-86d9f2f5943c | -9.5512 | -66.033302 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 787ac5f9-6a75-3a5c-bb07-aeb155d51713 | -11.7545 | -50.799801 | 2026-09-22 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecdb619a-0915-3cc9-a7d2-4e521904515d | -6.0869 | -57.665798 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7558449f-18d0-31fd-8581-63ce19c2f93f | -3.6012 | -59.437302 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec46f29-2239-3a79-9a4b-9a026beecc05 | -6.1011 | -57.682201 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee55fb76-4600-3773-bdb2-80f92b609bef | -3.4575 | -59.5294 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2431e30-e9b1-30b2-a50a-158f9441a25f | -9.6604 | -54.333401 | 2026-09-22 00:57:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| beb45b12-1f6f-3f0e-9539-5d3856348273 | -7.5798 | -57.655499 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f3ea78a-b5d8-33d7-80c4-2e9ffdc97932 | -7.5916 | -57.662201 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6c552c-c978-3ace-8212-3be1c59beb4d | -12.818 | -54.029499 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7de687cd-a19d-3cda-9004-490e68022526 | -6.7517 | -59.060699 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e096293-9776-3831-93f4-88971c0f83b1 | -3.4158 | -60.202301 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a75e7f2-1301-3062-b568-37c99c08eeb0 | -6.6312 | -59.9258 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f248ed63-7875-3edb-89f2-30def19e87f9 | -6.0315 | -57.825802 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8118b142-8424-3c09-ae6e-06e3cda563ab | -6.0957 | -57.7033 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e387e908-7f84-36e2-8908-fd7f1066f8bd | -6.3831 | -60.013199 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4834685e-0186-3bf8-9fbe-0d08a10a3330 | 0.1702 | -60.651501 | 2026-09-22 00:57:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b3e35240-67fd-38ed-9d0c-0451ec7861a0 | -5.9331 | -59.984501 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83639222-b47f-3e3b-988f-f0639869b073 | -6.6278 | -59.911098 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85118858-8a09-3dd8-b8de-adc0c7bb500d | -6.1163 | -57.747501 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a45e52f-7ef3-3843-96d1-ce1dcda6dc29 | -9.5588 | -66.020897 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 847e0511-c29d-3552-af07-b39df65c5c3d | -3.9194 | -60.5564 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb4e2b3-db7d-35e3-bb33-bcae1fdf8f95 | -10.5224 | -54.4809 | 2026-09-22 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 188a2871-e4da-3850-8abe-34eb199ea9cc | -6.4419 | -59.999802 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbf8edc8-9de4-3968-8ccf-bfb6f26ec4c3 | -7.6963 | -61.528599 | 2026-09-22 00:57:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83949ce2-1650-35dd-996e-0df09e2fbe01 | -3.8949 | -60.584801 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d16f1aa-ecab-3cc5-a369-b7c735e631df | -3.6824 | -60.6021 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af37c691-cf33-3125-96cc-192cbf7b01f8 | 1.7776 | -60.233398 | 2026-09-22 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
