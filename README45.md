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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e4c96f8-c7e5-37f0-8697-5d32a57c1917 | -8.2857 | -43.963 | 2024-11-18 14:10:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 77526475-a2b8-31c8-b609-5fc124b5d8f8 | -3.2898 | -42.6918 | 2024-11-18 14:10:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7a675742-b3e8-39e7-9b5b-2697356c71c6 | -6.9424 | -42.8126 | 2024-11-18 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 8c5a8c3e-837f-377a-8940-851ba8b38b5f | -4.6776 | -44.5861 | 2024-11-18 14:10:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9e1f3430-a626-352d-93e6-c8499e901d4b | -3.0285 | -42.6797 | 2024-11-18 14:10:00 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 8ec882f4-d533-3f77-ad2d-a6de60fd10b2 | -6.9236 | -42.8144 | 2024-11-18 14:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 0dbe5315-6d08-3fda-8d60-562f16eecd26 | -8.2854 | -43.9863 | 2024-11-18 14:10:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 6f4ac120-e3fb-3076-8e3d-7254cbb1334f | -3.8846 | -43.1544 | 2024-11-18 14:10:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e96a505f-58a1-3dec-9152-687ab96c6552 | -4.4038 | -43.7064 | 2024-11-18 14:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a9d527b5-223e-3ae3-8184-8e9e8033ad57 | -8.2665 | -43.9883 | 2024-11-18 14:10:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 778fd9a8-bfa3-3584-98fb-92de16ec19fd | -3.4173 | -43.2705 | 2024-11-18 14:10:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| da731270-6c48-36a1-97d3-f7ea4c34d529 | -8.2668 | -43.9651 | 2024-11-18 14:10:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| ca896d48-afcd-317b-b714-927e9e083d3c | -7.8865 | -44.2134 | 2024-11-18 14:20:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 18b72b2f-ca3d-3fe0-990d-18c633f0fe38 | -8.2857 | -43.963 | 2024-11-18 14:20:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 6a6ad866-246b-3885-8a42-9c0f59995e4a | -4.3968 | -44.7389 | 2024-11-18 14:20:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 30336b64-f943-3e53-9a59-57fd79f64068 | -3.0285 | -42.6797 | 2024-11-18 14:20:00 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 64371944-b387-3cc4-997f-13d8aa92243a | -8.2665 | -43.9883 | 2024-11-18 14:20:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 469.2 |
| 3b264233-a1e8-35d0-9dc3-f90ce09760b3 | -3.8111 | -42.948 | 2024-11-18 14:20:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 216cf9f7-d70c-322f-bef8-5482465a78db | -4.0148 | -43.2408 | 2024-11-18 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a35475ff-ac93-30ab-ac3a-2a68812232c3 | -6.3964 | -44.7396 | 2024-11-18 14:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 474.6 |
| 7f7aeb06-bd7a-3a84-bd48-a4110cb8b986 | -3.8846 | -43.1544 | 2024-11-18 14:20:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 215d4169-38c3-3733-a8cd-96794992b883 | -8.2668 | -43.9651 | 2024-11-18 14:20:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 359.8 |
| 71b7ef5f-5f38-3a6f-a614-6fad8d62150e | -3.8847 | -43.1311 | 2024-11-18 14:20:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d5ae08a7-c368-3348-aad8-0b496fec2410 | -3.8846 | -43.1544 | 2024-11-18 14:30:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| ea93b3b3-2bb5-32d4-9da7-27355ad32e6e | -4.1826 | -43.2781 | 2024-11-18 14:30:00 | GOES-16 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| da9ddeba-cfe9-39dd-b58e-2a41b0ef7622 | -8.2857 | -43.963 | 2024-11-18 14:30:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 707ce225-7d84-3bd6-969c-448148eb8eb4 | -3.8111 | -42.948 | 2024-11-18 14:30:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 00a61dd9-5ebf-327d-aaf5-92d57f783fd2 | -4.1201 | -44.2745 | 2024-11-18 14:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| dee65384-3eda-35fc-95f1-2e8458054cd8 | -3.8847 | -43.1311 | 2024-11-18 14:30:00 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4e3be047-8a09-3ea0-a7c0-f38822baa8e7 | -4.0148 | -43.2408 | 2024-11-18 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 75ad5a5c-ecf9-3861-84c1-d6bf005a511b | -8.2854 | -43.9863 | 2024-11-18 14:30:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c5ae15b3-9367-35e1-b86b-ec9db968a6bf | -7.8865 | -44.2134 | 2024-11-18 14:30:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 0e090516-ff26-365f-a9b9-b406c34bf489 | -4.3851 | -43.7075 | 2024-11-18 14:30:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |


