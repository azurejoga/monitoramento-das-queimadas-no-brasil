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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8136bbdf-d7b7-3edc-bd10-dff32fe472ce | -12.29058 | -47.64403 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 74d349ea-9a82-3546-84c6-54ed2ca55e01 | -12.28989 | -47.64912 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 309eef0e-294a-3096-a6cb-abd242a21bd7 | -12.28918 | -47.65422 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed815322-8226-3359-b411-93c2c769e236 | -12.28848 | -47.65933 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 95cb2175-6139-3e5e-b4f4-002a59f7063b | -12.28666 | -47.64345 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d146e9b9-113d-331d-98b8-7599e60d795e | -12.28596 | -47.64855 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2d30fdc7-aeb4-3d3f-ba50-6b3930ef2301 | -12.28525 | -47.65368 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ebf80f93-634e-3168-8358-c92757605d1f | -12.28273 | -47.64288 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5ca02c24-faf8-3dec-b65b-27dfed830ce0 | -12.28203 | -47.64799 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0cfed78e-ce3a-3707-af00-dfeaf7793ac5 | -12.28133 | -47.65314 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 71c6f157-e199-326a-86cb-964f2121c463 | -15.02264 | -47.55379 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 149a6b50-28f4-333e-a7cc-d1b96ea0d50b | -15.01856 | -47.5531 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d029e879-8ea4-3e4f-ba2f-8cc60e3c7c85 | -14.82675 | -47.68478 | 2024-10-02 04:49:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| af96d563-df6b-3b6c-bb3f-4276e1753a81 | -14.78998 | -48.07243 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3585aa0e-f3d4-3686-8395-8b24ec163615 | -14.78927 | -48.07756 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65be8c4a-436f-3a50-8af4-f9d3829cd10d | -14.78877 | -48.07449 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d3aa40e-54d5-3679-bbbc-199cae9a9df3 | -14.78603 | -48.07181 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e36f7c0d-7a0d-32f8-9f5a-2856dc2c7bc4 | -14.7855 | -48.06867 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9019809-5ead-3291-8d51-458d8e5f28a8 | -14.77542 | -48.09031 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30ff1c60-9a68-39b4-9fdd-f3548ed29d39 | -14.76106 | -48.07752 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a8f7f9f-7b35-36e6-b56f-afc0b8388bf1 | -14.75715 | -48.07665 | 2024-10-02 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dcc0ff7-efa0-3bff-a423-b8e528723c13 | -13.73845 | -48.15024 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae633cc0-eeb4-36aa-923b-35297a1d5428 | -13.73776 | -48.1553 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb786603-b0a9-3f0f-bbf5-982a85421f6b | -13.73584 | -47.58485 | 2024-10-02 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afc6aff8-922c-3d77-aae7-680105cf3512 | -13.73183 | -47.58417 | 2024-10-02 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90f1504c-4fdf-3b3e-8deb-4a457e605768 | -15.55543 | -48.04903 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63ead0cc-184b-390a-8219-785024e598d1 | -15.55331 | -48.04977 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db0b192-2893-36f8-b36f-414ae720fc96 | -15.55286 | -48.05303 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dc6a3f2-27ca-33c0-92aa-44e9a694cb54 | -15.55098 | -48.05188 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2325243-39c1-3df1-a634-03a1da0f35c1 | -15.55054 | -48.05527 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6422ef0f-17e2-3ae5-a5d5-223836b5f359 | -15.54884 | -48.05259 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdf2005f-3c1e-3a46-897d-4f6953fd320e | -15.54838 | -48.05594 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21ecbfd7-0594-3c24-98bb-de36f6cdf6e9 | -15.54439 | -48.05535 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 704d39f0-4d4a-3618-bf61-bf16e590e1a0 | -15.3714 | -47.42496 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9163f0b-8f20-3c9f-9789-7c8def54fca1 | -15.36674 | -47.42822 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a52b196-e337-3754-b921-83202edb9db8 | -15.36622 | -47.43225 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc752585-dece-39cb-9eda-9fee094c4800 | -15.36165 | -47.43484 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9f3ebfa-db1a-38cc-b94d-277a6efc8a3f | -15.28582 | -47.48096 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1879930a-8a42-3684-bb5d-f43d342d3c16 | -15.28151 | -47.51323 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0aa32a3c-6213-3955-a9f7-3bbefa3ac0c1 | -15.28091 | -47.51772 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7447284c-4390-38e4-b584-a7bc52c5a020 | -15.20763 | -47.94012 | 2024-10-02 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b25ae9e-e570-32af-a79c-aa7d019f13e5 | -15.20714 | -47.94378 | 2024-10-02 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aa6df94-1101-3c67-a648-132f735714b7 | -15.2057 | -47.95446 | 2024-10-02 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f460bf26-2279-3417-86cd-a3243098c4ff | -15.20312 | -47.94324 | 2024-10-02 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a07f5426-d355-3749-b3ee-cf0156a9e7fe | -15.19509 | -47.9422 | 2024-10-02 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39504591-f3e0-3b26-8839-0e579c9d5109 | -15.19461 | -47.94578 | 2024-10-02 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4316b130-0774-3fa8-aa40-2588850e3d3d | -17.86553 | -49.08412 | 2024-10-02 04:49:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48f4eb70-a1a2-3d01-b1e4-d0f18b9d2362 | -17.73361 | -48.4506 | 2024-10-02 04:49:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c2f2eca-c59f-3c48-8338-708554644dc9 | -17.73314 | -48.45423 | 2024-10-02 04:49:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca05d22f-e822-340a-be21-fdda332a6bc4 | -17.73265 | -48.45797 | 2024-10-02 04:49:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea9bd0c4-c4f5-3b2f-83b6-d077cfd1b4d9 | -18.20924 | -48.65669 | 2024-10-02 04:49:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6ff4bfa8-cfc0-300b-ad5d-1d214bdd837c | -18.2088 | -48.66013 | 2024-10-02 04:49:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f9896d1-126a-3984-9a27-31285641f3a1 | -18.20482 | -48.65944 | 2024-10-02 04:49:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0dc721fa-90e8-3ba8-98cf-1a385c4c3e7e | -18.20037 | -48.6624 | 2024-10-02 04:49:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e99e79fc-dc8a-3cd7-b8ae-5f2e37ad0e55 | -18.04953 | -48.60162 | 2024-10-02 04:49:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3956bd44-43a0-3bec-b124-923f915f48db | -13.20679 | -48.61732 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c22f5532-0d4f-3395-a0ee-3ea9f968e15f | -12.27194 | -49.21095 | 2024-10-02 04:49:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75885d90-9864-3048-8c7e-329aca392889 | -13.75622 | -48.3069 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9280f38c-4f59-3080-929e-158208463113 | -13.75555 | -48.3117 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 675d803e-843e-3491-ae67-3e20e0157e53 | -13.7549 | -48.31633 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f964eb49-e9d9-37c9-9ef1-dc2ddfcc015b | -13.75239 | -48.30623 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0e10fb6-ab6d-3034-bd55-4cd0fde87399 | -13.75173 | -48.311 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d06de29-f430-3462-af50-a3dcd4838d03 | -13.44541 | -48.56766 | 2024-10-02 04:49:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f0efd52-e529-3fa2-b497-1ee35af0a669 | -13.19439 | -48.50925 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e95caaa5-7857-3312-b376-dee3941fd3d5 | -13.26205 | -48.57824 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b26a5b4-8253-35c2-b0ac-7f4e16772eb7 | -13.26141 | -48.58281 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee1e5c0d-2032-3059-98fc-2f5f8cf78180 | -13.2583 | -48.57761 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52e925ef-3570-3948-a239-d513ff8c9e6e | -13.25766 | -48.58222 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 181b4adf-9998-3923-9f1f-36b167405bed | -13.25702 | -48.58675 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9bda719e-b1c1-3c1f-90b6-6d2a99f6cb9b | -13.25455 | -48.57697 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59222062-0593-3fdc-a726-33f97807924b | -13.25081 | -48.57627 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a86dbe8-7c96-30a1-aad0-8b49dad92ac4 | -13.25015 | -48.58095 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 55cc8444-d509-3782-8a42-1896051c9d11 | -13.24951 | -48.58559 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 51f63da0-4938-38d2-8c38-b4345f4ee9f7 | -13.24641 | -48.58027 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c68c54f0-c5ae-39fc-8723-fdc6d30f4198 | -13.24575 | -48.58498 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f3d98cb-accd-330c-abe6-1b5e975a55b4 | -13.2451 | -48.58963 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70dd7e46-c3ce-3bf9-a18b-3ea4ff1c4721 | -13.24136 | -48.58897 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20c7958c-7893-3fa2-bb85-cb2f58aa189b | -13.24072 | -48.59359 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96481cb6-7c1b-3424-af54-461f87060223 | -13.23954 | -48.57445 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a1caeb3-f1cf-3cd5-9ece-7246f6819d28 | -13.2389 | -48.57906 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a80ac083-aa91-33e6-b131-9891bf3f09cb | -13.23696 | -48.59298 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 381ea0ad-e543-3166-b52a-15cc1ab34743 | -13.23579 | -48.57388 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70733c3f-ef3e-3f8a-903d-62b20fe2e615 | -13.23266 | -48.56874 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33b5002f-23a1-39fd-a98a-c9b50e476324 | -13.23203 | -48.57326 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8ddb7d7-1499-32f5-a897-c5f9ae94f38d | -13.22828 | -48.57266 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7521610-94a8-30ef-a0eb-010309e3db61 | -12.98493 | -48.5401 | 2024-10-02 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 915a3e9f-f7de-3d28-a471-dfa5e6f9d911 | -13.49612 | -48.61752 | 2024-10-02 04:49:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b947994b-8d16-33d0-a8a1-4e9a33a2ac3b | -13.49546 | -48.62219 | 2024-10-02 04:49:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e4e8ccb-fe7c-3f2b-8401-446849d72f16 | -13.49237 | -48.61688 | 2024-10-02 04:49:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a16c144-cd6d-3455-b8f7-3c2a1a5186c2 | -13.46474 | -48.62216 | 2024-10-02 04:49:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95c4e239-cf63-3d87-a414-7710d0439dcd | -13.45034 | -48.61528 | 2024-10-02 04:49:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e08ea954-47a5-317a-874c-7a1303332aa5 | -13.21238 | -48.6322 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b0683b-feb7-3a1e-bbf0-1c4c6c5898fb | -13.21188 | -48.60167 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6985139f-2ba6-3e26-b18c-540b5b1736d8 | -13.21181 | -48.60865 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 552f2780-4a04-3262-9528-576c9eeba9d8 | -13.21119 | -48.60643 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 288c0247-8050-31c7-a2a5-18011fe17720 | -13.21117 | -48.61328 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b55feb9-7ef4-3853-838a-e2921c0f3efc | -13.21054 | -48.61789 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b268afb2-4f67-3ade-94ca-dd15d9f9f5ec | -13.21052 | -48.61108 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd886f6a-8c3a-394c-b9c2-e4def62fafaa | -13.2099 | -48.62247 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d056bc18-0cc1-3234-8060-08d079484c9f | -13.20986 | -48.6157 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README96.md)
