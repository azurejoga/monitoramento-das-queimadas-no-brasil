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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e08eb192-13fb-3704-ad29-9a366c786e26 | -6.42713 | -55.79701 | 2026-07-02 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 163a94d5-558e-3269-b91c-e28bace2890d | -13.6538 | -60.6213 | 2026-07-02 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6170f5b-b6cb-3222-aa3c-8914ef52cfa8 | -8.72015 | -48.33417 | 2026-07-02 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d8433119-b3f9-34cb-8876-6459ec2cf754 | -19.49886 | -52.72936 | 2026-07-02 05:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fa06901-5e5c-301c-9ab2-abf2840972f7 | -8.65641 | -49.70841 | 2026-07-02 05:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3fd173c-5cd3-3e4e-8978-19c692552802 | -11.90597 | -57.38196 | 2026-07-02 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ffd6d8a-6595-3463-97eb-feb4de27e28c | -8.72369 | -48.33982 | 2026-07-02 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01bd2e6b-c24d-3318-9f0d-1f499d00bfd4 | -12.41891 | -58.39458 | 2026-07-02 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ae0e8eb-c1e3-3b30-b067-4ee01af33339 | -11.80735 | -57.00231 | 2026-07-02 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cf5f3b66-7eff-3e04-84a8-dd037d33d2f5 | -12.41954 | -58.39027 | 2026-07-02 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6939c08f-3e2c-3f97-95e5-fda21fd1eefe | -15.44067 | -55.87186 | 2026-07-02 05:25:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de40f912-8995-30cf-866a-176fe456b9e1 | -21.80111 | -52.72366 | 2026-07-02 05:27:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38d4be40-35a0-38e6-808d-9339ac2374d6 | -21.78128 | -56.29372 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6d0d6ce1-bc40-3710-a097-fcecd96d674b | -21.77657 | -56.29319 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b5c4d537-b117-3ed1-a18c-5fa1d05e0cf5 | -21.77241 | -56.28741 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 8b0dd31d-6dbf-3f88-8d90-eb0b6016614a | -20.70431 | -50.52216 | 2026-07-02 05:27:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 365c309b-dec1-30c1-99ea-4051da93c259 | -21.76987 | -56.29199 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 2ee9c780-0ef7-3d3e-a3f8-7317e9351891 | -21.76715 | -56.2921 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 21141ea8-85db-38ae-924b-fe27d82038f7 | -21.78184 | -56.28846 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f27377ba-f985-3d77-b7d5-b6a9edad32c0 | -21.77712 | -56.28795 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c6073c4d-ed69-31aa-aa30-cd425b0592d1 | -21.80347 | -52.71833 | 2026-07-02 05:27:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b6ace28-388e-3790-bd48-df280ff31aa8 | -21.77186 | -56.29265 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 6fa0e42a-2487-3cca-9be8-bf01e50cc817 | -21.80304 | -52.72309 | 2026-07-02 05:27:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 577e1e68-d934-37dc-aae4-f240245949de | -19.81878 | -54.64751 | 2026-07-02 05:27:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ffe9353-e457-3a2c-a4d7-d20a3be7ba89 | -21.45544 | -51.36478 | 2026-07-02 05:27:00 | NOAA-21 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 431c69ec-b3a4-3700-964b-65f58fb698eb | -21.77046 | -56.28675 | 2026-07-02 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 323ea941-c9f8-3152-8cae-483df479744d | -21.80743 | -52.71944 | 2026-07-02 05:27:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2656cc9f-4f2f-334a-b585-cad0a56f445d | -21.45732 | -51.3644 | 2026-07-02 05:27:00 | NOAA-21 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 69c8ea3f-ba8d-3b54-8a15-eb00198bc93e | -12.8548 | -44.3625 | 2026-07-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| b2e75061-7058-3650-b833-50e2bf49869a | -10.9397 | -43.0593 | 2026-07-02 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3bde59aa-831f-3d53-998f-1c2c9a8c6d1c | -12.8741 | -44.3593 | 2026-07-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 5508ec9f-b57c-3b4b-a9a1-3c8a204b5c1d | -21.7823 | -56.2976 | 2026-07-02 05:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e3a777bf-6856-3d54-a65e-8eee018c8ee5 | -12.8557 | -44.3154 | 2026-07-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 0eaf5c93-3102-3580-9816-9a50cd0772f6 | -12.8746 | -44.3357 | 2026-07-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 9ca6c00e-2298-33dc-8a97-80ab3e22293f | -12.8552 | -44.3389 | 2026-07-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 349.0 |
| cd17f80b-86dc-3a7b-a938-08480b5dfaa4 | -12.7369 | -44.4756 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 35a83139-1556-3131-a518-d32aae2b67b5 | -12.8548 | -44.3625 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 82b37892-aa02-3874-af67-f3b5f34279e5 | -12.8557 | -44.3154 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ee5508fc-d115-32d1-9151-5ab3893161b0 | -12.8746 | -44.3357 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 83251dd2-5bd1-3b34-9c83-ead882cf54f2 | -12.8552 | -44.3389 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 333.0 |
| 805c7adf-2de4-33e1-a315-f019d5a1192a | -12.8741 | -44.3593 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| a4c012c6-aa9e-3110-b691-97bb6e3baee8 | -12.7755 | -44.4693 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 77b457f5-73d3-375b-971b-89ad8292ced3 | -12.7562 | -44.4724 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 332.9 |
| d2277e74-57ef-38f6-9448-e1bfb13533d2 | -12.7751 | -44.4927 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 264f077f-d824-32a6-a1ed-3248729501ef | -12.7557 | -44.4959 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 232.1 |
| e17f0781-a661-361f-89f7-95feaa5e96e5 | -12.7746 | -44.5162 | 2026-07-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 61025d34-e174-325d-9487-fef40db0c31d | -12.8746 | -44.3357 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 250.0 |
| f8a09e90-a084-347c-825c-2b2ec25ca139 | -21.7823 | -56.2976 | 2026-07-02 05:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 78.0 |
| cfeccb32-8ed0-3e0f-a25e-ea8fc45eef80 | -12.8552 | -44.3389 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 325.4 |
| 57ebf76e-4dbd-3fcd-95da-ee30c72fef86 | -12.7369 | -44.4756 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 09931de7-a12b-317a-bc01-eee9bed32a2e | -12.7557 | -44.4959 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 221.6 |
| d69b83e6-837d-31f2-8ca1-67f3c2509ea4 | -12.7751 | -44.4927 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 6cce3d10-6edf-3538-b6ef-152fe4ff049d | -12.7755 | -44.4693 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 3304aea5-e680-3275-a5e4-63b5d3f7004c | -12.8548 | -44.3625 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 49a80026-957d-3e3b-82e6-4a77705fa7a2 | -12.7746 | -44.5162 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 95e123d6-771c-37bb-a7ce-adf0c47af7dc | -12.7562 | -44.4724 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 263.8 |
| 3a8d64aa-d109-385a-be16-64b939048ac7 | -12.8557 | -44.3154 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 633e2226-11b4-31d1-8c71-ba0f75321717 | -12.8741 | -44.3593 | 2026-07-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 211e52b9-419c-328e-a8ba-dd546ba194bc | -9.18009 | -58.06808 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edd1ccc8-41fe-3645-9a19-568e091c2fa5 | -11.80283 | -57.00286 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da55f218-e9fe-38a7-b6e6-0dfd58117013 | -11.36059 | -55.42939 | 2026-07-02 05:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b12c67-916d-35c4-bff3-142744d6562a | -9.18807 | -58.0503 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae55c57-734c-3076-b9dc-84f26a208b61 | -9.17503 | -58.06359 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 317c2315-35c0-3931-b541-d4b46b4a86d3 | -11.80861 | -57.00499 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3370578c-d4e8-3493-9e30-7d79cd80e76d | -11.41533 | -56.06908 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 12786c76-3968-3ee5-af80-cbf35df88b72 | -9.25887 | -57.85954 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 855ec9a0-e7d5-3611-82ac-1532a59bf562 | -9.02512 | -59.53858 | 2026-07-02 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0f23f4b-9733-32c0-bcb7-f0b720d58823 | -11.41653 | -56.06332 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9bfe28f8-b403-360d-9a37-1c9b577ff2e5 | -9.19311 | -58.05491 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b6fe10-a5a3-3069-a4fd-1cf5473d2e5e | -11.35644 | -55.43147 | 2026-07-02 05:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dcaf668-fb06-31f1-96a2-2dcfcfd59c3f | -11.80842 | -57.0082 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9441ab5-193b-3a5c-b45c-841ed6a7523d | -9.19361 | -58.05118 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcce80ba-0447-3de0-b328-6aecfaf2c580 | -11.42235 | -56.06956 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 800a11cf-7cce-38fe-bbfc-5ba5f1bda550 | -9.26103 | -57.86374 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f90ad9ef-bc92-3202-9fbf-1ef4105da85d | -11.36317 | -55.43226 | 2026-07-02 05:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f4e91a1-2f6a-31bc-a136-6d33614dc23b | -11.80226 | -57.00752 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e92d7b84-4e40-3b50-9b62-b4fe3b0f3f20 | -9.17407 | -58.07096 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a11d06dc-9eef-3fac-82c5-2263e810f9d3 | -11.4218 | -56.07005 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4d4e1a3-f030-3576-a17e-a37e4b2cb842 | -11.42241 | -56.06478 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2ff4372-f632-3e2f-9847-b98dddbf428d | -11.62926 | -59.0191 | 2026-07-02 05:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bdfffe7-da34-3ac5-a70c-73a15cc11ddd | -9.19965 | -58.04821 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b7912a8-3930-3944-9ff2-bbeadb5aa071 | -11.36384 | -55.42635 | 2026-07-02 05:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 157bf46f-6b1f-3ef7-9639-084fcb1d5a98 | -11.80192 | -57.00893 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 74463087-b9dc-3d51-b299-76cdce8867e3 | -11.35989 | -55.43526 | 2026-07-02 05:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f6a8677-d20b-3402-b582-3dfed06f82b1 | -10.81769 | -58.01772 | 2026-07-02 05:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51bf02bb-d424-3beb-97f4-43579e29d47d | -11.42364 | -56.05902 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 559ac96f-6314-3f55-aee3-e1f2a329a46b | -11.80807 | -57.00964 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f76c3e16-e7c9-3e03-9eb1-e11f57637d6b | -12.1545 | -57.22755 | 2026-07-02 05:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15e7461d-d134-32dc-9092-6ad379f4d1db | -12.14843 | -57.22661 | 2026-07-02 05:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212b3d8f-244f-37c7-b4eb-792538c5012d | -9.19263 | -58.0586 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83327bc0-a9a2-3f24-9537-b085b193810e | -11.63508 | -59.01644 | 2026-07-02 05:59:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c274acb5-0b3f-3090-8cf6-70b14e186acd | -9.02433 | -59.54435 | 2026-07-02 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1767c6a-b355-37df-b610-640046233956 | -11.42302 | -56.05948 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0a28b5e-8d8a-3158-a54f-819b227f3bb2 | -11.80899 | -57.00358 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9de3857e-6ab0-38be-a001-e8965afa7ce3 | -11.41589 | -56.06861 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1f6d7b02-545e-3ce9-9f9a-39952c697db9 | -9.25837 | -57.86328 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be660273-26e2-310f-9b87-88d2208f491f | -11.79632 | -57.00335 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f3af3d74-e944-333a-9df6-44ac2a3d63f5 | -11.80245 | -57.00425 | 2026-07-02 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cb84d5ad-afa9-35db-b54a-9ca826a33b41 | -9.26151 | -57.85996 | 2026-07-02 05:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66021d62-c4b1-3276-85cd-f67aff612ff6 | -11.41594 | -56.06376 | 2026-07-02 05:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README24.md)
