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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b2dbf26-fe18-3a26-9e4f-981b1a484d99 | -7.90982 | -45.42236 | 2024-10-29 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 20a9c041-3fa8-34b3-a2ea-14201a1ba648 | -7.9213 | -45.42404 | 2024-10-29 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| f55a6330-480d-3411-a6e1-ffe807321c4a | -8.25224 | -44.86457 | 2024-10-29 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 2eacc113-3e5f-3009-a610-c828335298b1 | -8.77984 | -44.72454 | 2024-10-29 12:14:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 957a695c-dd77-3d54-9ee9-80371de675e9 | -8.86282 | -45.37039 | 2024-10-29 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 07edaa9d-c5f0-365c-bc25-f74a99d4fd20 | -8.87169 | -45.38722 | 2024-10-29 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ea699496-215a-3d76-aa2d-3474ff15d88d | -9.02797 | -45.19375 | 2024-10-29 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ced506fe-d525-3f21-8be1-75952aa25a12 | -9.09035 | -45.53258 | 2024-10-29 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6b4e4405-c921-35e5-ac78-86dc569771f3 | -7.07725 | -45.2317 | 2024-10-29 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0ec6423c-63ca-38cc-a63c-6dc5922e48c1 | -7.07963 | -45.21613 | 2024-10-29 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 53e59ff1-ab53-3597-9869-e8e4b44583fd | -7.38717 | -44.26291 | 2024-10-29 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 9ce56068-f9d0-38f8-9e78-e0d1a050f98d | -7.39776 | -44.26449 | 2024-10-29 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cd7ab494-3c88-3397-b734-cb42c47be30a | -7.39975 | -44.2514 | 2024-10-29 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 33.3 |
| cbea360d-bcb9-33c5-9eb5-2d767473ba1c | -5.28318 | -43.41322 | 2024-10-29 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1768.9 |
| d03f1ac2-ff8c-31dc-9d5e-b322476d0d4a | -5.28502 | -43.40108 | 2024-10-29 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ab30b569-4bd5-37f2-9156-56be55d173cc | -3.83561 | -44.14801 | 2024-10-29 12:14:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1108965a-d8e3-3669-8fd4-7b0d377ee883 | -3.83775 | -44.13348 | 2024-10-29 12:14:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f95b6d4a-f209-3745-81b3-f508355dbbd9 | -4.03966 | -43.24407 | 2024-10-29 12:14:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| fba71c4f-b3d5-34e3-9d71-7e04e4096a9a | -4.33849 | -43.78444 | 2024-10-29 12:14:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1630.1 |
| 12e93682-9ad1-34fc-9cbe-dd3fb030b00c | -4.34047 | -43.77112 | 2024-10-29 12:14:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 595.7 |
| b158acff-1485-3ed8-b5f0-4d7ec58102cf | -4.52508 | -43.48025 | 2024-10-29 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0a155bae-79ca-3205-a32c-0e5b875e6e68 | -6.59026 | -42.27471 | 2024-10-29 12:14:00 | TERRA_M-T | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 5fccb7eb-eea0-3a05-9228-7d6d19ecec24 | -6.84915 | -42.81479 | 2024-10-29 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| f725e836-cd2b-3a4d-bf62-e61259edcd34 | -6.85076 | -42.80414 | 2024-10-29 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 204e616f-158f-3df9-a68c-c2a32ae1980a | -6.85881 | -42.81622 | 2024-10-29 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| 25724276-3d44-36d2-a82c-c5e5947ae980 | -6.86041 | -42.80563 | 2024-10-29 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 86f3c5c3-4fde-3c3d-a1cb-f3b2f0f51c66 | -7.01782 | -42.6313 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 1da9de74-6333-3dfa-9afe-453a3e4b378e | -7.29734 | -43.64242 | 2024-10-29 12:14:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| eb2a0e06-d978-3273-8bf0-fc76e73c754d | -7.88106 | -42.96042 | 2024-10-29 12:14:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 694caa7a-85ce-37be-a246-fd2cb1ac6573 | -7.88265 | -42.94978 | 2024-10-29 12:14:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 1c95b57b-e606-3770-9bcb-bd84f65994ff | -5.37925 | -43.25003 | 2024-10-29 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6be01a16-adaf-3c96-9d7e-7624a245c555 | -5.87823 | -42.29814 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| f78e6255-5009-3b68-9bab-51f0a41311df | -5.88353 | -42.2948 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 2d944957-a86c-3a59-b43d-11224eda70d1 | -6.12338 | -42.51144 | 2024-10-29 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 5121bf1a-76ae-34df-a21f-93793637a288 | -6.12655 | -42.5181 | 2024-10-29 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 03b6b036-2056-3dfa-b731-e189f1115c27 | -6.12815 | -42.50754 | 2024-10-29 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 9d235052-fd33-3685-8f01-57e45f7ab1a8 | -6.13613 | -42.5195 | 2024-10-29 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 0907b490-898f-361b-9549-d7f0bc13ca35 | -6.13773 | -42.50897 | 2024-10-29 12:14:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| e37e4fce-cd8e-3c51-9fbe-0769d3dd7f6c | -4.86798 | -42.63088 | 2024-10-29 12:14:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| ae6c43e3-eb8a-3006-9b46-c41824a18953 | -3.67875 | -42.36668 | 2024-10-29 12:14:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 6acb20b9-bd53-35fb-bd99-45525dfb6eda | -3.68037 | -42.35581 | 2024-10-29 12:14:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| dd827df5-ec2e-3c74-bd22-66f4777bbbd7 | -3.73735 | -42.30828 | 2024-10-29 12:14:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 238.6 |
| 8494c61b-e883-3f9c-bce4-b654ff88d810 | -3.73894 | -42.29739 | 2024-10-29 12:14:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 810.7 |
| f540c8aa-6277-3e1a-a7b7-e499bf8e4c50 | -4.85984 | -42.48497 | 2024-10-29 12:14:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 992ae515-a5ac-3da6-88bf-b7008626529e | -4.86146 | -42.47419 | 2024-10-29 12:14:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 8e76e43d-668e-38cb-861d-d9915d5bf466 | -3.0004 | -42.44669 | 2024-10-29 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a6385d3b-46d1-3073-b9d6-b23e74f3298a | -3.00195 | -42.44144 | 2024-10-29 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 32caf605-996d-39ed-ae43-4cf02e3db8d6 | -3.00203 | -42.43542 | 2024-10-29 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 81c102ce-d1ef-3e94-998f-483cd7522eb8 | -3.00365 | -42.43016 | 2024-10-29 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 63030e35-7192-3cb7-9246-2fc0866432cc | -3.15398 | -42.17592 | 2024-10-29 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| da6c605e-7c5d-3d23-8c8b-7574b335997b | -3.1556 | -42.16508 | 2024-10-29 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4b72646c-5dc7-3a82-9b91-6dc6a14d0b05 | -3.25664 | -42.30824 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f3147c6b-b644-32fc-99ab-12719fe4856e | -3.49165 | -42.16597 | 2024-10-29 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| e7a0e6d3-5557-3c52-8c2a-586d2ad8e1e4 | -3.49981 | -42.17805 | 2024-10-29 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3d72f390-1913-3cec-8585-f797677598fc | -3.50137 | -42.16729 | 2024-10-29 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| aa39f6cc-1ba8-317e-8953-f98c59f12fc9 | -3.54206 | -42.17976 | 2024-10-29 12:14:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 97272763-b8c0-3429-9f61-eda5e97a3a54 | -8.3488 | -41.67167 | 2024-10-29 12:14:00 | TERRA_M-T | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| e72742b3-35d9-3abd-b027-d3b569418517 | -8.35016 | -41.6624 | 2024-10-29 12:14:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fc4a6145-5260-3c66-993b-b930c544255a | -8.56806 | -41.43458 | 2024-10-29 12:14:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5334102c-26a4-382c-85b7-679b155b8e88 | -6.68305 | -40.89279 | 2024-10-29 12:14:00 | TERRA_M-T | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 4fe57940-b262-3a5f-a678-01e18fc7a826 | -6.99629 | -41.33496 | 2024-10-29 12:14:00 | TERRA_M-T | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 5f7cd2a3-8aea-391a-ad94-a5becaff9a66 | -7.01296 | -41.34681 | 2024-10-29 12:14:00 | TERRA_M-T | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 452d54b6-c846-3ca9-ac54-6b7d1ed23985 | -7.01431 | -41.33759 | 2024-10-29 12:14:00 | TERRA_M-T | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 1f394fcf-da84-3a50-a9ef-e5eb7fdaa590 | -7.33127 | -41.87354 | 2024-10-29 12:14:00 | TERRA_M-T | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| cf5e4893-1bc4-3eec-ab36-35ad9d4393de | -7.91166 | -40.93946 | 2024-10-29 12:14:00 | TERRA_M-T | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 64c0b929-4a45-300e-abe4-9890ce142730 | -6.35213 | -41.57844 | 2024-10-29 12:14:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 52feb6d3-7fb2-3b7c-ae28-456605cbc9f2 | -4.40287 | -40.71722 | 2024-10-29 12:14:00 | TERRA_M-T | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 1f6538ff-6af0-3a3a-b966-742bd9b45372 | -3.22794 | -41.18238 | 2024-10-29 12:14:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| d117c202-7bce-307f-a0e8-397add3f9d27 | -8.40078 | -40.88274 | 2024-10-29 12:14:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 17fee936-ec14-34f8-855f-521488fa36ff | -8.68021 | -39.70805 | 2024-10-29 12:14:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 14754ee0-ffd7-3e59-8f0f-3f3d7b2388ac | -8.72139 | -40.82932 | 2024-10-29 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 57673083-addf-35f6-9a2e-b75cb37cf29f | -8.80289 | -40.96553 | 2024-10-29 12:14:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 803535e3-9351-3d25-b5f4-2245bc6d615b | -8.97515 | -39.96131 | 2024-10-29 12:14:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| df7319d1-a7b2-3156-83ef-70608da3001b | -9.19255 | -40.05684 | 2024-10-29 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| edf05a48-4c10-3227-ab8d-949175c9accd | -9.23919 | -40.62547 | 2024-10-29 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 52367a2c-fe0e-3c6b-bd3a-2f9540cc8913 | -7.10224 | -39.5857 | 2024-10-29 12:14:00 | TERRA_M-T | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b0d0b18a-d5fe-3d3b-b729-9ae568090818 | -7.17902 | -40.14378 | 2024-10-29 12:14:00 | TERRA_M-T | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ea03ccc9-6980-3c30-88e9-62dc2f36cb57 | -7.1803 | -40.13492 | 2024-10-29 12:14:00 | TERRA_M-T | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 04b480ea-3981-3ce5-b176-439f0f10806b | -5.28495 | -39.47532 | 2024-10-29 12:14:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 8d096ca8-0f5a-3a62-89e0-717eafdb3134 | -5.29381 | -39.47656 | 2024-10-29 12:14:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 3601d3e1-3025-3203-afd7-45c7fd72083e | -5.48037 | -38.88005 | 2024-10-29 12:14:00 | TERRA_M-T | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 0850097c-95c4-37d6-8842-bcc83844cae3 | -5.75013 | -39.05574 | 2024-10-29 12:14:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| a463767a-49ae-3351-83a2-f110fdcb79d4 | -5.75142 | -39.04672 | 2024-10-29 12:14:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 33db6b7c-1f57-36ec-b48d-4958ddbe6b4d | -4.67596 | -38.89553 | 2024-10-29 12:14:00 | TERRA_M-T | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| bf82cdcb-0a19-3085-93f7-a8d3e7b36a3e | -8.45891 | -38.52314 | 2024-10-29 12:14:00 | TERRA_M-T | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 90c4c4ff-7ccf-31cc-b854-b924d15b270a | -8.46027 | -38.51328 | 2024-10-29 12:14:00 | TERRA_M-T | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 84a992f9-3c0c-3611-8cbd-d77ab4e0066b | -6.67836 | -38.22396 | 2024-10-29 12:14:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 18.6 |
| bed2f56c-85c0-3903-b947-cea3c7e8d456 | -6.67973 | -38.2142 | 2024-10-29 12:14:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 5da7ea47-6be6-3ccc-ba75-1014d6df0265 | -6.70478 | -38.50171 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 40.9 |
| 80aa2f71-53bd-327c-8341-efc5d133ce5c | -6.71202 | -38.5087 | 2024-10-29 12:14:00 | TERRA_M-T | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cc9e12f8-c112-3c3c-ae8f-06d108413ae4 | -6.79703 | -37.96434 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 10.1 |
| be4fbec4-6fe7-318f-9770-a83e4c3790d7 | -6.92862 | -38.09059 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 78ed4853-becf-31e2-9108-1c37299de4ea | -7.00166 | -38.41194 | 2024-10-29 12:14:00 | TERRA_M-T | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 8320e4fd-ec77-3b64-b811-08b9fb73dfd0 | -7.82792 | -39.02547 | 2024-10-29 12:14:00 | TERRA_M-T | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 47d2eb18-f658-3d75-a290-3146f5bb1a07 | -5.29043 | -37.16437 | 2024-10-29 12:14:00 | TERRA_M-T | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 809c0bf5-4df1-36da-9a93-b61af44dce2d | -6.23044 | -37.88529 | 2024-10-29 12:14:00 | TERRA_M-T | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 436ad1ed-0cd7-38b1-a1e4-75f88d09503f | -6.41226 | -38.54911 | 2024-10-29 12:14:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 83f073c3-cacd-3780-9100-fb69dd2d6b22 | -6.41362 | -38.53963 | 2024-10-29 12:14:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 56.5 |
| d04529ff-5815-3219-86ed-f2087a4fef98 | -4.18831 | -38.37481 | 2024-10-29 12:14:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 0e78f3bb-61d3-3323-bad8-ba33d3ce61dc | -8.273 | -37.6223 | 2024-10-29 12:14:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 99.9 |


[Clique aqui para ver as próximas entradas](README107.md)
