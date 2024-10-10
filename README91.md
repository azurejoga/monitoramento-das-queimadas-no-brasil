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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69c5d6e6-8b7c-35df-9ba8-7c12293e8785 | -2.89793 | -50.70644 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41ee4de4-c660-343d-ae59-c7c833e06d82 | -2.89738 | -50.70989 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3994cfea-9540-3821-8587-59ebe0a30b99 | -2.81518 | -51.59839 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7835ca22-b65d-3b92-b678-f1688b2865e8 | -2.81181 | -51.59787 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea2452c4-706a-31f6-bb8f-384313c7ab4b | -2.80972 | -51.39333 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1821f28d-d667-3531-a9b9-6b620182f0d5 | -2.70468 | -51.3912 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76e345da-c40f-3331-b9fe-a7678edc4648 | -2.63669 | -51.75463 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1168d45b-3ac8-3fb5-b236-80cd8358be79 | -2.63331 | -51.7541 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2aa1157-a0f0-3577-a745-02978bd397b7 | -2.62992 | -51.75358 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7acdf912-858b-335d-a216-8adf345e6018 | -2.58225 | -51.92149 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9be4e54-3bfb-3ab3-9e4e-60fa2d9497d2 | -2.58166 | -51.92515 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95a81864-1cb0-3f0d-b4ee-fcd847640d87 | -2.27354 | -50.65796 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3575ec2-314e-3182-8eb8-17e107c05a6b | -2.27299 | -50.66142 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 745f521e-be92-33c9-8387-2fddc50e942a | -2.27023 | -50.65745 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f19eb7f8-4350-3662-884c-e0ddfdab7ac9 | -2.25121 | -51.66195 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cff300d8-83ef-3496-8c0a-778875ceb154 | -3.34336 | -51.67303 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bcca5fe-e081-3de5-a92e-b4854f9e9a86 | -3.26202 | -51.24036 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28ae6797-5fe2-38d9-bd40-d6c690677e7c | -3.25869 | -51.23983 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f8d3088-8718-34ee-a3a4-df892a48609a | -3.2356 | -50.84813 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c696c2c-a01b-3565-93f3-99a09ee5c645 | -3.23229 | -50.84761 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d29a9819-d57f-382b-b179-4a1064fc181e | -3.23174 | -50.85106 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6437761-495c-3f4c-8813-779f1f409008 | -3.22897 | -50.84709 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b702d3b-ae63-304f-8b80-d17699694da4 | -3.22843 | -50.85055 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eef6486c-1b7d-336d-8cf9-5bda2a9ca3b3 | -3.20479 | -50.9142 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3b54323-1d69-3710-91a9-9837ebe766e9 | -3.20093 | -50.91714 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4e16a92-03b7-339f-82f2-12e4791b9d7d | -3.18134 | -51.23522 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e5fce6-95e6-3407-99c5-65379d292737 | -3.17801 | -51.2347 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e558997-1d7a-3e8b-8848-80cf3a756992 | -3.17745 | -51.23819 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94a4f4e7-511f-3b17-bac1-cba6d46c857d | -3.17492 | -50.88828 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 234348dc-df0f-3a38-af13-75226d08f067 | -3.17113 | -50.8912 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57e98519-eb80-38d1-9f13-18690c94d5ef | -3.16781 | -50.89069 | 2024-10-10 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecf9c1cd-dbd9-328e-b7ec-651bcb6065c3 | -4.09387 | -51.02874 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2158e45-0fe6-31ee-b2b3-de3eb1f342f0 | -4.09278 | -51.03568 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf88f94f-523a-30c9-8ebf-5878f702e56c | -4.09165 | -51.02129 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae4fe5fa-114e-3852-b7b5-d703435460c0 | -4.09111 | -51.02475 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 16b9baf4-c4c0-36cd-9e8e-1cf30cb61729 | -4.09056 | -51.02822 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a9edc878-a70b-3c4c-81b2-7d0455f0d585 | -4.09001 | -51.03169 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ac4a709-1780-3f5b-8a21-1864152bcfd1 | -4.08947 | -51.03516 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bbbb739-f72e-3f54-b2c9-c43ab84030ed | -4.08834 | -51.02076 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c14d3ad-7dc3-3b40-9669-f28e6121d041 | -4.08779 | -51.02423 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f73ad7c9-237f-37e7-9a4e-832961967abf | -4.08725 | -51.0277 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d78942e9-a8ee-3d60-b8a6-cf2112100bf3 | -4.0867 | -51.03117 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 809aa4d6-ecd8-3d0d-af4a-d2e5b554412a | -4.08615 | -51.03464 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0df90f93-b0ab-3fbf-83f4-415df0e43fb8 | -4.08561 | -51.03811 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c2497bd-73b9-3daf-a39c-7b566b0d31e9 | -4.08503 | -51.02024 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ae032627-12e5-3546-b694-a55b524767be | -4.08448 | -51.02372 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 52eec104-cd63-3b1a-8a14-347ea6fe5e9b | -4.08394 | -51.02718 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 649750ec-8e51-3c0b-90b8-b1fabb589990 | -4.08339 | -51.03065 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f36fbdfc-16c4-3844-8589-86d2be6edf00 | -4.08284 | -51.03411 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3499874-6377-3214-86b5-e0e7f1ae3b5d | -4.08117 | -51.0232 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dab524eb-a2da-36c3-aff0-09958a936e7c | -4.08062 | -51.02667 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8be7c0e1-b863-3231-9584-dcd8b154c1ac | -4.08008 | -51.03014 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80a570b3-b0e2-3b58-b2fb-5515b7038f0e | -4.06641 | -51.11673 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86394403-89d0-39bb-a13b-3b5dc8fec122 | -4.0631 | -51.1162 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b4ff354-01fe-3923-a69c-db7b7501ca64 | -4.06255 | -51.11965 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f687918-fcee-31c3-9a14-2f8f0bb5d1d3 | -4.05869 | -51.12259 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 424096c2-b40f-3ff2-8499-ac227ceceeb7 | -4.05643 | -51.09387 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f25cd89e-5dad-3b4e-a7b7-4d914a174468 | -4.05206 | -51.12153 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ea601d-3e3a-3514-8bb0-afd997285140 | -4.05035 | -51.08937 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c84e27-1557-393a-80b5-3c67a036e69e | -4.04929 | -51.11755 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 674c9a63-bca5-3525-9bfd-b9ee8d09b2d2 | -4.04703 | -51.08885 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5aa714f-7a2b-31c9-8b1a-d9a26c3b18ea | -4.04652 | -51.11356 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fba09daa-904f-3bb7-87fd-dabd4ff45b0d | -4.04598 | -51.11702 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfaed92c-c69c-3d4a-8f5a-b6f4fa304aa2 | -4.0432 | -51.11306 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebd6f17b-fabc-3bfb-9320-dd77e359f6eb | -4.03048 | -51.10758 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ee04f6-b030-352c-90fa-d4fa5db9787b | -3.90883 | -51.0171 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e60b206-cdfa-39a5-a5bc-260872c501b3 | -3.8912 | -51.82091 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48dfa217-90f9-3806-ab26-b3678ee8e404 | -3.888 | -51.93793 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa301be2-fa75-30fa-99d0-8b4b371610da | -3.88784 | -51.82038 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15caaa6e-32ae-34c8-b5f6-d0fbd4957de1 | -3.88463 | -51.9374 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64f9da5d-95b9-3bb1-af9d-95fecd3f8c77 | -3.85063 | -51.25724 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2a3c6e-4077-3272-94ce-c86cfcd1b419 | -3.84731 | -51.25671 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b53207e6-0843-3e2f-8c7c-14f8aa546e52 | -3.84676 | -51.2602 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b537331-e05a-34d9-9d1c-f717cd39807f | -3.84668 | -51.92798 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 982f4e12-6df2-32a3-a2b7-d36d4223c504 | -3.84453 | -51.25271 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6ca78ec-4976-331d-990f-705d8d84302f | -3.8433 | -51.92744 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27e7c2fe-43c6-393c-9bfa-cc156e0d12bc | -3.84181 | -51.2916 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb09b89e-e9bb-3617-991b-232f9433b6e8 | -3.84126 | -51.29509 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76b2f374-3841-3e22-90d6-132ba74d8fdd | -3.84066 | -51.25567 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51baad63-8bbf-3148-8d36-2afb73601b68 | -3.83993 | -51.92692 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d83470d6-c3ab-3dd7-8a85-b336b3a68a94 | -3.83793 | -51.29456 | 2024-10-10 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f878cb55-61a0-3ddc-be3f-b7a18d00b7f7 | -3.79441 | -52.21419 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df52e570-26d7-3948-92c4-6fc2b1b6d70e | -3.68848 | -51.1218 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2fe2f6d5-b8d1-3a06-a01d-cf65cb52f47c | -3.68793 | -51.12528 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a27e00e9-bc4f-38c0-87b7-377e2c4c0cf7 | -3.68738 | -51.12876 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69107490-790b-3615-b8d9-1990f444420c | -3.68683 | -51.06784 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a2023e63-c561-3965-afe3-79d284e4d710 | -3.68628 | -51.07131 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cdb3ae76-f8aa-3574-a8a7-e7ea54327de6 | -3.68516 | -51.12129 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 19acde14-e163-38ea-b003-68d2b4c2b09d | -3.68461 | -51.12477 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c6431ef-3a66-341a-a9d0-4f60d7410ce9 | -3.68406 | -51.12825 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c322005-fce8-31cb-aa92-1d99cbf4f843 | -3.68296 | -51.07079 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 68e9dde0-4cd7-399d-b97d-59d6837afac1 | -3.68239 | -51.1173 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1c1e0715-ddfd-382c-a7f9-e34a262bf0a6 | -3.68184 | -51.12077 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ee53d89e-9198-3bc3-98d1-4a3ca3c6a206 | -3.68129 | -51.12425 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7087bee-c32a-33aa-bb7c-4666c5628e28 | -3.68074 | -51.12773 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 21dcdc48-e098-3719-ab77-9bd74a113291 | -3.67864 | -51.11996 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 210864e8-3e45-361b-9283-ecd421433cfb | -3.67809 | -51.12345 | 2024-10-10 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e7fa5f45-7d46-323a-8abf-5b023e7fbc80 | -3.6727 | -52.11987 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47c844e4-b1da-3cd5-97e3-0f1142f44ee7 | -3.66989 | -52.11568 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e0cafd6-77a8-3bdc-aba8-5ab9564d9631 | -3.56057 | -52.05444 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README92.md)
