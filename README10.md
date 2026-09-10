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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 760b277f-5176-37f5-a96e-757ae4ace83f | -5.7571 | -45.0613 | 2026-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ff759b0f-4977-36e5-86f5-7a8f002c26b0 | -13.4453 | -43.8366 | 2026-09-10 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3b5f67e3-a972-3c0d-a4f4-c14b71bc3add | -10.7769 | -45.96 | 2026-09-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| eb69a29a-506b-33fb-acc6-9357f5d01e77 | -5.7569 | -45.084 | 2026-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 313.4 |
| bf4e2ad0-235e-3dbb-9845-4400930a602b | -6.5453 | -62.8914 | 2026-09-10 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 145.6 |
| c5648428-25ee-321c-9ea9-86521d89686b | -10.7772 | -45.9372 | 2026-09-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 5ea60d86-ebf2-3fc7-8e5c-ada49325715e | -13.4453 | -43.8366 | 2026-09-10 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 54d00eb5-7ecc-3e63-b200-eb2fd1816c43 | -5.7754 | -45.1053 | 2026-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5b7c6fa6-6e6b-3fa4-a853-98589dc8559c | -5.7569 | -45.084 | 2026-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 285.1 |
| 12c72c5b-e2c1-321e-88a9-8ec6e97cabc2 | -5.7758 | -45.0599 | 2026-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b7f81941-0b2d-3539-b529-fecc5716bf51 | -5.7567 | -45.1067 | 2026-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 18d38254-039d-38e2-9d7e-8e0f9430654a | -6.5453 | -62.8914 | 2026-09-10 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| cda8c899-bb9b-3072-865b-ab722bc9e182 | -10.7582 | -45.9397 | 2026-09-10 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| de1ce413-bea1-3499-a9b8-cba43a02da19 | -2.7331 | -57.6271 | 2026-09-10 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| de7ff3b7-d5be-3a7d-a09a-6acb0f683f36 | -6.7695 | -58.6097 | 2026-09-10 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3170a0a2-b96b-32f7-b23f-d8608a7b19f2 | -5.7571 | -45.0613 | 2026-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c0c40568-0cc4-3a4b-827a-9bec3da0985d | -10.7772 | -45.9372 | 2026-09-10 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3e47d8e1-0dfc-3279-a29f-a055c8aa2c91 | -10.7769 | -45.96 | 2026-09-10 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 482a096f-2d01-3783-a915-7eec55cc33ca | -6.5452 | -62.9102 | 2026-09-10 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e441d30b-a823-3c67-aad8-e176cb665c7e | -5.7756 | -45.0826 | 2026-09-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 336.0 |
| 1ebada4d-5761-3428-855f-6124bfb39fed | -10.7578 | -45.9624 | 2026-09-10 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 8febf198-38a4-30c7-a7a4-244185997029 | -6.5637 | -62.8908 | 2026-09-10 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 924bd3f1-0b06-36f9-971e-2db05c1cbe39 | -13.4453 | -43.8366 | 2026-09-10 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 3c0f4f45-652a-3629-85c1-1a1058b25365 | -5.7571 | -45.0613 | 2026-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7fee9600-a9d4-32d0-a2fd-745af14d0d9b | -9.1626 | -58.3143 | 2026-09-10 01:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c67c037a-dc39-3a3b-abb7-29b5a994cc75 | -6.5636 | -62.9096 | 2026-09-10 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 73d153cc-d47a-3772-b012-0c03c02600e0 | -5.7756 | -45.0826 | 2026-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 276.7 |
| 0ef3d071-dd29-36fc-9172-d939314ed9c3 | -5.7569 | -45.084 | 2026-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 5dc9d4e7-2783-3fd4-9fbd-4a253b300f35 | -2.7331 | -57.6271 | 2026-09-10 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| b7f5bf93-c4b6-3a88-8c0d-6fbf0fd4e608 | -10.7769 | -45.96 | 2026-09-10 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 289.5 |
| b1f1ca5d-3599-347f-9771-d5d4112ecb8e | -4.9335 | -42.8813 | 2026-09-10 01:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| abf29fe4-e737-3bf2-88be-c5d6a3b0b6ff | 0.2483 | -51.4597 | 2026-09-10 01:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a170e24c-ff20-3963-bcaa-4fbb7db14814 | -6.5453 | -62.8914 | 2026-09-10 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| dea53355-34af-3692-80b3-1a2b493eb4df | -10.7582 | -45.9397 | 2026-09-10 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 9ae0766e-acd3-35ac-a4a3-fd3098f2d6f3 | -6.5637 | -62.8908 | 2026-09-10 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| bbe5f6dd-dc66-3588-bad8-f4ba143ff19f | -5.7754 | -45.1053 | 2026-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 40906bff-eb3b-30a7-89ab-2d31d236ccd5 | -10.7772 | -45.9372 | 2026-09-10 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 55d9a1ce-17b9-39a4-bac3-c9881d38dcf9 | -6.5452 | -62.9102 | 2026-09-10 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8785b56e-b70f-3ea3-8c68-a7be629a1730 | 0.2667 | -51.4597 | 2026-09-10 01:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d7d14cf9-7a48-382a-a897-23b237371f36 | -5.7758 | -45.0599 | 2026-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 8e79e833-51d2-3f2b-9d04-8267d8ef44ec | -10.7578 | -45.9624 | 2026-09-10 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| f735747d-20ba-329d-b28b-541bed73ca1a | -5.7567 | -45.1067 | 2026-09-10 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 47f36c12-d05f-3ba8-af34-a10a130ad09b | -5.7754 | -45.1053 | 2026-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 19b5224e-d75a-3e64-aba4-fbd831f84183 | -10.7765 | -45.9827 | 2026-09-10 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 4d8930bc-b970-35c2-8798-5b807cfda3ec | -6.5452 | -62.9102 | 2026-09-10 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 57afb08d-4c33-3eff-a694-11f56740cd53 | -6.5637 | -62.8908 | 2026-09-10 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 83688f8e-6bf7-306d-b2df-520444369c19 | -10.7772 | -45.9372 | 2026-09-10 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 70343de8-8141-35c6-839f-acb1ed15057d | -5.7567 | -45.1067 | 2026-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 3287afbd-6e2e-3b87-a511-bc341eeafd6c | -5.7571 | -45.0613 | 2026-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 92a874ba-f0ac-3cef-a7a8-beb2aeaa9a54 | -2.7331 | -57.6271 | 2026-09-10 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| eb592e33-5776-30d8-a102-cdba01ab4669 | -6.5636 | -62.9096 | 2026-09-10 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ad9d2552-42dd-3e8d-8502-3c9ccf7796d2 | -6.5453 | -62.8914 | 2026-09-10 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 27ad7e06-c0cb-35d3-9c86-6e7325189470 | -10.7578 | -45.9624 | 2026-09-10 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 190e83b5-7675-3663-8b72-025f15956fc3 | -10.7582 | -45.9397 | 2026-09-10 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ae359d2e-8c7c-3ac8-ad7d-46abb3211ec3 | -9.1626 | -58.3143 | 2026-09-10 02:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| bfca93b0-b281-3bee-b63b-a31f49fec9b8 | -6.7695 | -58.6097 | 2026-09-10 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1d7d44bb-452f-3c2b-ae62-96821a24b8b5 | -10.7769 | -45.96 | 2026-09-10 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 310.6 |
| cea4f104-d4b3-3e1f-8bde-afe897777ba8 | -5.7569 | -45.084 | 2026-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 288.2 |
| 000dcdc9-e28e-3caf-a7fc-94b8fe098b25 | -5.7756 | -45.0826 | 2026-09-10 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 1d53c10f-7099-3b54-a926-eae7abb8e074 | -6.5452 | -62.9102 | 2026-09-10 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 031b7e0f-5684-3ced-bc53-e66a111b27ce | -6.5637 | -62.8908 | 2026-09-10 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3cdab6a7-c208-3a7d-9e2e-20b29d5a3f72 | -6.5453 | -62.8914 | 2026-09-10 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| d7fe0434-fb7a-312f-82ac-c3fde86fe4a5 | -20.558 | -57.4771 | 2026-09-10 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 500a62a2-ec9a-39f1-8dfa-4c35febd87a3 | -5.7754 | -45.1053 | 2026-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0d108065-6c79-3f45-8eeb-840433fcb396 | -10.7578 | -45.9624 | 2026-09-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 2c8cf0cf-408d-3b18-9048-58192159a25f | -20.5584 | -57.4561 | 2026-09-10 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| ee6e329b-fb61-3a98-9f84-b1bab22b2f7a | -5.7567 | -45.1067 | 2026-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a78c0476-1203-3715-ad9d-9e89ea10232e | -9.1626 | -58.3143 | 2026-09-10 02:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 7b672758-5b05-3cbf-be0c-cf3dd993dc7f | -10.7769 | -45.96 | 2026-09-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 61e61748-28dc-33dd-8318-079283b5bd5c | -5.7569 | -45.084 | 2026-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 98d0e49f-7277-3c42-a64f-bd2184f48eae | -5.7758 | -45.0599 | 2026-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 983905e0-4b8a-3b12-885e-6a7326e2e30c | -7.9834 | -43.9951 | 2026-09-10 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| b62aff19-65d3-346e-b9c4-ffc15a5d6895 | -20.5381 | -57.459 | 2026-09-10 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| c20b5ac1-60fb-3de5-8caf-71db342df9c5 | -5.7756 | -45.0826 | 2026-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 282.5 |
| c3ca71d3-32ff-303d-a419-f06e80fc6198 | -20.5377 | -57.48 | 2026-09-10 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 08bd1c6e-b0fa-3cf1-a347-909205a7a4c7 | -2.7331 | -57.6271 | 2026-09-10 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 5034adfc-2414-3f89-bc1f-e4c270fa404c | -12.86 | -44.36 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 574c095e-de1e-3a88-92f3-8fe084e2b682 | -12.86 | -44.31 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc228f42-7431-380d-8999-bd69f2f638aa | -12.86 | -44.41 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c76090ee-30f0-3fc2-85ba-bb0514719785 | -5.76 | -45.09 | 2026-09-10 02:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8403bf30-8e11-39d0-984b-5b3c3799d25c | -10.77 | -45.98 | 2026-09-10 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22a5da6f-6998-3a08-b609-4d3aa8ef8517 | -12.83 | -44.35 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80c30e9d-1e41-38c6-a72f-53480c4fe2af | -12.89 | -44.37 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31b57812-59d4-30e0-874a-4a6c23933cff | -12.8 | -44.34 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 470d7afe-d1fa-383b-90d9-d12820908a07 | -12.83 | -44.3 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56716da0-a71b-31cf-807b-0d40172a190d | -12.83 | -44.4 | 2026-09-10 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c19e8726-5faa-3451-b4f2-5709227bf3e2 | -10.77 | -45.94 | 2026-09-10 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d23799f2-c238-3898-81d5-d586cba2f2b8 | -5.7756 | -45.0826 | 2026-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 8ff422bd-274d-3552-b2e9-b7f86e973e06 | -6.5452 | -62.9102 | 2026-09-10 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 84e95805-7b53-3680-8f07-f683e92d8632 | -2.7331 | -57.6271 | 2026-09-10 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| f7658093-6dda-3b71-b0cf-d2859847f9e9 | -6.7864 | -58.8801 | 2026-09-10 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 01c06908-ffff-3705-be57-b2a8298f765c | -5.7758 | -45.0599 | 2026-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d78f2125-565b-3757-bd0b-a846e50d5b52 | -9.1626 | -58.3143 | 2026-09-10 02:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| bfcb1d9a-110a-32c1-b2d7-2dafb98e4270 | -6.7863 | -58.8995 | 2026-09-10 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 2e6c370f-0c15-3a5c-89d1-c56765825b58 | -9.006 | -65.4 | 2026-09-10 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 6223ffd2-eaa9-39c7-8255-3d6e33790f88 | -5.7569 | -45.084 | 2026-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| c8e587dc-ec6d-3064-bf1d-2ec3972f0213 | -5.7567 | -45.1067 | 2026-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 64f9b042-6f7d-3fe2-b1e6-c14e2ab1383d | -5.7571 | -45.0613 | 2026-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 09450776-d797-3d03-b2d3-9f705b889ccf | -6.5637 | -62.8908 | 2026-09-10 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 4f028ed9-d8f7-3bba-8d24-8127ba5f0136 | -6.5453 | -62.8914 | 2026-09-10 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |


[Clique aqui para ver as próximas entradas](README11.md)
