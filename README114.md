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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fa54cdf-019a-3062-a38f-34380d7fd0f1 | -3.29867 | -50.16443 | 2024-10-25 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 01646d61-c520-3772-9735-ee7dcdbeb82c | -3.25734 | -50.20133 | 2024-10-25 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 7a168dec-1647-39a3-bf4e-f8d6c699af48 | -3.25594 | -50.21101 | 2024-10-25 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 480daa93-b053-33ce-b0d3-1dba286fdf20 | -3.22471 | -50.16744 | 2024-10-25 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f74afa53-60a9-3cb6-99bd-fb4c826bda02 | -3.15397 | -49.77096 | 2024-10-25 12:49:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4d7dbeda-7479-3c82-a946-60860a2d83e8 | -3.1525 | -50.46392 | 2024-10-25 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 23792fef-8bfa-387c-b902-133a1cae0e06 | -3.14719 | -50.45659 | 2024-10-25 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3d053b03-c65b-3a3d-b4a0-d02d864efeb6 | -2.95896 | -50.52507 | 2024-10-25 12:49:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4ec2f61-8994-3164-86d0-3c18c5f44f5c | -2.9228 | -49.58478 | 2024-10-25 12:49:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| be8e6e3e-3a3f-358e-86ac-bccefaa6f279 | -2.86879 | -49.44962 | 2024-10-25 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a32de636-6991-33ca-bcd6-0bb168c4a3fe | -2.86746 | -49.45871 | 2024-10-25 12:49:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 81a19c80-c719-3b2d-a1ed-ccfa342da244 | -2.8043 | -49.25904 | 2024-10-25 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 023a13b5-c35e-3f95-a105-67786e53f947 | -2.79667 | -49.24878 | 2024-10-25 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| b14a8500-4d57-3af7-9069-fe8d7c8156b7 | -2.75049 | -49.30957 | 2024-10-25 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| aff59859-f51d-3d7a-b3c0-d4c15124a77f | -2.65712 | -49.50978 | 2024-10-25 12:49:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7e92fd8c-9e19-3dc9-8d24-3c189be92abb | -2.64061 | -49.242 | 2024-10-25 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4b6e54cc-64ea-3c48-b96b-1075d52ef262 | -2.60517 | -49.10225 | 2024-10-25 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d557114e-0dda-349b-b89d-d178437c1ca5 | -2.49154 | -49.38088 | 2024-10-25 12:49:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 609b38de-428d-3e48-a90d-13cd01957a53 | -2.49021 | -49.38998 | 2024-10-25 12:49:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 742cace9-be60-3700-9bfa-a0a1b4ca4b4b | -2.4844 | -49.29969 | 2024-10-25 12:49:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 9d991eb8-e820-338f-bdb4-3e58cd9bf758 | -3.87791 | -50.05273 | 2024-10-25 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 36d9e977-cb72-375d-bde2-6a4ffc61635b | -3.66411 | -50.12503 | 2024-10-25 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3636a8d6-d8d0-3826-9044-53ad2262f501 | -3.6569 | -50.11803 | 2024-10-25 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3910cd74-c128-352e-835a-5c18b68db984 | -3.65554 | -50.12744 | 2024-10-25 12:49:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e3bfb38f-4cf3-3b95-b602-1b5f8fcc8698 | 1.9382 | -50.89014 | 2024-10-25 12:49:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5a9f6c76-d542-33ee-8dc6-9abfc93b7d36 | 1.78602 | -50.46889 | 2024-10-25 12:49:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 5e409966-b622-3905-892e-b98555a43cf6 | -2.18067 | -50.5016 | 2024-10-25 12:49:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 06935ec9-e6ce-3431-bb5e-939ca6a34c4b | -3.08424 | -51.25445 | 2024-10-25 12:49:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b44152ab-2e61-3196-a477-b1f9e2454f19 | 0.65012 | -51.86617 | 2024-10-25 12:49:00 | TERRA_M-T | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f4f3bc52-0b54-36ba-be76-8d780adf4288 | -1.11042 | -52.23339 | 2024-10-25 12:49:00 | TERRA_M-T | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4df533d8-fc2a-366c-8da7-256eefb992fc | -3.04352 | -53.24531 | 2024-10-25 12:49:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 85e72cde-49f6-3fb6-b821-e8f1e5127ec2 | -5.28802 | -43.27195 | 2024-10-25 12:51:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1056a575-7b98-3ee1-b2a0-c8e56edadac9 | -11.28002 | -40.61077 | 2024-10-25 12:51:00 | TERRA_M-T | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 63.5 |
| 37b58cbd-2168-37b0-afe1-0844208e0e5a | -11.27056 | -40.61682 | 2024-10-25 12:51:00 | TERRA_M-T | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 26cd6fb8-1498-30d4-a1b8-e74bbda3dd8f | -6.99013 | -41.51242 | 2024-10-25 12:51:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| c7a94e14-87f4-316d-9f30-8420bebd12fd | -6.98713 | -41.53621 | 2024-10-25 12:51:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| bbd9b63f-403f-35fb-83e0-5137c3019318 | -6.98372 | -41.5298 | 2024-10-25 12:51:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| f884b31d-3ed3-38f1-9b5c-669e53435a19 | -12.13971 | -42.43737 | 2024-10-25 12:51:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 47.8 |
| e2d90ec2-f981-3171-9bc9-a0643d69c09a | -12.13737 | -42.43017 | 2024-10-25 12:51:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 743716ff-6ec5-3d09-9d67-949d84bb5338 | -11.09258 | -41.53431 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 1d9d139e-ece8-3831-a5d4-21bf75864b96 | -12.72144 | -43.16549 | 2024-10-25 12:51:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 9e7c97da-43b0-3158-9d83-987207ed80bd | -12.71875 | -43.18872 | 2024-10-25 12:51:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 8830fed7-8657-3190-b088-f8c3eaa5b0bf | -12.57341 | -43.22968 | 2024-10-25 12:51:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 4e9b3306-898b-3143-946d-2240d58a9567 | -12.50277 | -43.24454 | 2024-10-25 12:51:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| c893936a-141f-3ace-8273-c13f29be48cf | -12.44172 | -42.43522 | 2024-10-25 12:51:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 0f9e781f-aa2f-3123-bd99-d91cefbb5e3d | -5.95271 | -43.27911 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 5702474f-5ef0-3c11-b9c7-a1414f2b1dfd | -5.26312 | -42.95799 | 2024-10-25 12:51:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 28.8 |
| b9ff672e-cb92-3b89-8be5-5db61666a1ad | -5.17706 | -43.23326 | 2024-10-25 12:51:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b72fb28f-eb57-3047-8c44-51ed0fb93c26 | -5.17222 | -43.22696 | 2024-10-25 12:51:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7571d638-4bb5-3ef5-8866-f8c0b2868eda | -5.06846 | -43.13652 | 2024-10-25 12:51:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| d2bfe552-8809-3bc9-85cc-2bd751584168 | -5.05073 | -42.99064 | 2024-10-25 12:51:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fb35e1a9-3939-3624-9933-f7ee32e178ef | -5.04738 | -42.98432 | 2024-10-25 12:51:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 96cfd2d7-14db-35cc-93b2-5d6af65f2f59 | -6.6788 | -43.03325 | 2024-10-25 12:51:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 62c8e07f-f0fa-3690-be9b-518b54293496 | -6.67511 | -43.04626 | 2024-10-25 12:51:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| ea289d88-c233-30a4-8d0e-c0042d827c1b | -9.34926 | -43.3774 | 2024-10-25 12:51:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 36.7 |
| b592479e-4fb0-3deb-b8c3-e01e78f66524 | -9.15643 | -42.63126 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO LOURENÇO DO PIAUÍ | PIAUÍ | Brasil | 2210359 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| dceedf28-6326-3eb8-9f81-dd9b02b89284 | -10.63276 | -43.33548 | 2024-10-25 12:51:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 113.4 |
| d6955c5c-5d71-37fb-9a9f-19a932005fc3 | -12.11962 | -43.6382 | 2024-10-25 12:51:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 815f49ac-8cbb-3a59-bd14-dacf6d7bad84 | -11.54414 | -43.97786 | 2024-10-25 12:51:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 4436efa3-9887-3c38-a380-21c6eb28070b | -11.54178 | -43.99702 | 2024-10-25 12:51:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| acf232ab-9eb6-307f-8096-4cbb5430e9a1 | -11.52921 | -43.99544 | 2024-10-25 12:51:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 978b3637-0d02-3344-9c02-81d4174077d1 | -12.53024 | -43.36181 | 2024-10-25 12:51:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 47d5ef22-529f-3e9e-9943-d836f23dd6cc | -12.52761 | -43.38408 | 2024-10-25 12:51:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 5ea8572d-fbc3-39af-b1ee-324a19bdcb68 | -5.07597 | -43.66687 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e2862c24-149c-394f-b47f-513697dbac25 | -5.06434 | -43.66537 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| b96b9e2d-34f4-357c-b7be-a02d3493fcba | -5.01888 | -43.58814 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 30aee56b-1d8a-3b90-ac19-8b52f578be68 | -5.01668 | -43.60417 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e0ede400-8f9f-35a7-b292-cf29a7d30ecd | -5.85694 | -43.75476 | 2024-10-25 12:51:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 564a36d1-06cd-3691-9bbd-4d6b65ef9436 | -5.45468 | -43.57811 | 2024-10-25 12:51:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f3ae8678-8167-3baf-b0e5-e5ede2c4bb18 | -6.38238 | -44.77836 | 2024-10-25 12:51:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9561074a-6d5b-30e7-bd66-cbc0971a59f1 | -6.12122 | -44.91584 | 2024-10-25 12:51:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| f3b2ebb9-1a16-30e8-a78f-d0c0a37edd91 | -6.1194 | -44.92906 | 2024-10-25 12:51:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| d4d7d086-e642-317d-a3c8-b47aace33d68 | -6.10871 | -44.92755 | 2024-10-25 12:51:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 5aa7fa05-56ef-34f7-a511-6d03cd66e922 | -7.23898 | -44.29105 | 2024-10-25 12:51:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d11d9787-bc1d-3633-b880-294a80b78bb6 | -7.23688 | -44.30648 | 2024-10-25 12:51:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 362d83fa-be8b-35f2-b4bd-d215506a5add | -7.23684 | -44.29657 | 2024-10-25 12:51:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e3be6251-87e1-3ccc-97b6-7a8f4774bef8 | -6.68688 | -43.95803 | 2024-10-25 12:51:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 84b55b0c-7509-305d-842c-b0034bcac9c9 | -7.29771 | -44.96045 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| f76c6154-263a-3b62-a679-2250ecdb686e | -7.29582 | -44.97443 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 9f964322-0fe2-34c8-9413-27230ffa5669 | -9.30001 | -45.24673 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 3d671df4-e7d9-350e-bdea-267baf37b6b8 | -9.28911 | -45.24481 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 261.1 |
| 7da203fa-e0fd-3e90-82be-5769b8cfa417 | -9.28717 | -45.25939 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 4f877209-038a-3b1e-b290-e4b3e60a15cb | -9.26896 | -45.31281 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 1673e961-1344-3169-b083-0f8a8c4bc72c | -9.26715 | -45.32652 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c3a1a3cf-efc6-3c93-9817-e546666263c7 | -9.25807 | -45.31124 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1845b793-5421-3277-897a-fec5fa4d448d | -9.25626 | -45.32503 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| f1870d95-07d4-333c-be56-0ff973c33b58 | -9.23251 | -45.25105 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b2b57b23-29f7-3bf6-889f-0742859998a8 | -9.10951 | -45.49463 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 00b58a75-7938-3cde-a2ad-43ab749f04d7 | -9.08086 | -45.51239 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 01e4c2f8-b287-3626-9a59-b62dcdc86af5 | -9.07906 | -45.52568 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5db103b6-11d3-33ca-ab7f-cc48a267b685 | -9.07574 | -45.04482 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 125c8968-c453-3f88-a262-b8d52c340ef1 | -9.07551 | -45.03792 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| d285e4a8-9e65-3250-9b72-dc5e4472ec18 | -9.07346 | -45.05302 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3187df28-fd60-3927-880e-91ff59b3ee09 | -9.06465 | -45.04316 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 119068a9-ab11-3bc5-881d-af22b36f778b | -9.06241 | -45.05126 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b2693a5c-79bb-3b01-949b-eedb6ae87df4 | -8.9978 | -44.93884 | 2024-10-25 12:51:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 134350ef-82ed-31f3-96a4-386ab17e7fd2 | -8.99584 | -44.948 | 2024-10-25 12:51:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 81dc222e-e66c-304a-ac6e-bb7f79b3b0e5 | -8.95649 | -44.9874 | 2024-10-25 12:51:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 05aa1e05-9859-3309-8216-eecad4aae7ae | -8.60715 | -45.1263 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1db81b2c-f8d4-39c1-993c-90bf85438ad8 | -8.60538 | -45.12002 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |


[Clique aqui para ver as próximas entradas](README115.md)
