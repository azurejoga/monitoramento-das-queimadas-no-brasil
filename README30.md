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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbe7ffbf-1e79-32ce-8fa5-99e2b1f6f8c8 | -6.26253 | -42.62459 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b3114070-6966-3196-b3e8-63569f26c361 | -6.16946 | -44.1152 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cd5c93d-b8e9-31a8-bb26-a7b456df2cc8 | -5.857 | -46.60823 | 2025-09-02 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ceda090-b9d6-37b9-8a71-29493afafe9a | -4.31266 | -48.09949 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fec2a0a3-a409-3544-b3f6-0b001d2e345c | -6.26247 | -42.60325 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bb2bcc24-a7c4-373c-be7b-4ec2e4a86d78 | -6.33845 | -43.52254 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5abe9907-117f-3932-8e4f-0915adf06ec2 | -3.59828 | -49.45905 | 2025-09-02 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b54f284-487c-3100-b937-84ea9823fa1e | -4.91827 | -43.20166 | 2025-09-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca982257-3a9b-36a1-bd25-2b8d60915ca5 | -4.47978 | -48.11798 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fef0c200-9151-3e79-a691-6f84a8bb267d | -6.52051 | -43.50874 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6115c9de-5ac5-32fa-afe4-c773125b4727 | -3.81775 | -41.06063 | 2025-09-02 04:12:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32fdd751-46a1-37c9-a729-e43a6efc18fe | -2.1402 | -48.00086 | 2025-09-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adc21e6a-860a-3836-b5e0-510ac39edb2c | -6.33697 | -42.56149 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f6b9fbf-71a1-3ada-91ce-3c9008a1ba1f | -6.33514 | -43.52201 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed14ad32-467c-388c-9b44-5e9b71f9cfb2 | -6.27531 | -44.51107 | 2025-09-02 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58a1415e-e847-31c7-b66d-ffe3b7b214be | -5.78527 | -42.59214 | 2025-09-02 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 14cc4c4d-750a-3b8a-a7bd-b9c883d6d6d1 | -4.90942 | -43.19318 | 2025-09-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f428a8a8-946a-32d2-a85a-f8f4d6143364 | -6.27039 | -43.52261 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97989885-0f9f-3080-8349-3159d1fd3e09 | -2.26061 | -47.84699 | 2025-09-02 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 622d3e5d-9b1a-37ba-bbc0-e2293716a123 | -6.39637 | -43.49975 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6185be8-0aa5-30d3-9a05-dd251e634f3e | -4.48041 | -48.11423 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 433145f5-ea87-33c7-aa19-2854e79bf7d0 | -3.16598 | -49.4825 | 2025-09-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f0bc8f6-6ab3-39b3-ad7b-486334782919 | -6.08944 | -46.72422 | 2025-09-02 04:12:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9bbe0c1-abf8-383c-a70f-bc484b5e9be1 | -6.34066 | -43.52999 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74773fe8-f89c-3385-b274-d0b645ed8aac | -4.07207 | -47.96172 | 2025-09-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fbdb848-31a0-385b-ae00-db4046ac1e62 | -3.59838 | -49.45706 | 2025-09-02 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 765af248-a313-332f-96fc-5dc1339c61bb | -6.14773 | -44.12262 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f00bdc08-ba0f-3808-9835-2142ad1dfe8b | -6.01895 | -46.01408 | 2025-09-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd74f70f-f4e1-3e64-9056-50f9325d10e2 | -5.50941 | -42.64065 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e0b02cce-0d79-3082-8cb5-1653b52f0da7 | -6.20469 | -45.38397 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d49d9c43-d058-33ee-9c91-82755df410db | -6.17614 | -44.11626 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16e898d5-af2e-3847-9f59-8b2bf81e6c88 | -6.27136 | -44.51411 | 2025-09-02 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c679b84e-f743-33ef-9058-db056af3499d | -6.22321 | -41.81225 | 2025-09-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 77700719-a967-39d4-b6c8-409a88be326c | -6.47975 | -43.57336 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b6b5752-d69b-3439-a06f-ebb52aaaf969 | -6.29036 | -44.39628 | 2025-09-02 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de431a89-c359-3964-83b2-9868c8866b94 | -4.29528 | -46.26283 | 2025-09-02 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 344da1b4-8939-3bc8-b8a0-dbcd435154ff | -4.30853 | -48.0988 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63265eb2-5778-3de1-bf55-47e571e59fac | -6.53111 | -42.94693 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5a41068-38e8-3e19-ac7b-2100460cf787 | -2.9068 | -48.29782 | 2025-09-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 993e2a74-4aef-3d92-a130-b96e23a36251 | -6.1728 | -44.11573 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d48a42a-f965-393d-a6ce-743a32010202 | -5.85627 | -46.61263 | 2025-09-02 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac6b047c-9bb4-3340-9f25-1ce54b7dbe71 | -6.54337 | -43.92262 | 2025-09-02 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd4b8fad-d0c8-3657-8b97-0a1dd2fbb704 | -5.91946 | -44.97652 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c8784fa-55cd-3796-80f4-7c96d69b1945 | -4.90611 | -43.19265 | 2025-09-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7848dcba-fb86-3804-a737-5f4643d2f7f1 | -6.2781 | -44.51519 | 2025-09-02 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2332453-3857-3e60-875b-fb9fbee82b1b | -6.29362 | -43.56892 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a27ef9ac-afa7-39c1-b605-33a06b865821 | -6.29372 | -44.39681 | 2025-09-02 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91ce1321-0bba-30e3-aa3b-6a46b0b5a2ab | -4.48391 | -48.11864 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1383b109-52b3-3246-be3f-b6a2389bfd20 | -3.22649 | -47.13211 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e0ad0b6e-01b9-3afa-849d-abce74d5f028 | -5.96811 | -42.96442 | 2025-09-02 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0c9e13ed-fd03-3e2b-943f-aa35ce6e5f62 | -1.98426 | -47.97719 | 2025-09-02 04:12:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 87e790c4-65e9-35a5-a597-4fc467a66525 | -3.38289 | -47.61558 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e76829bd-0887-33dc-8ff3-2837a0a5283e | -3.78657 | -47.56831 | 2025-09-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b46daa9-b59f-3b6b-8a7e-c0d9665fa11d | -6.27757 | -43.52018 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cf23a66-36d2-3605-89a3-465cfd7cd07e | -6.5444 | -42.97029 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02f755a9-7d47-3d75-9554-d68139bf38a6 | -6.29913 | -43.55556 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a64c039f-5bcf-3ea4-85c5-aea86afc7c67 | -4.30439 | -48.0981 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 111e8301-8f23-3454-a691-14a1c5b60379 | -3.16741 | -49.48118 | 2025-09-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9de44ef-c1cb-3c7f-912f-8e6a5e339a1d | -6.7199 | -42.26275 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 826c6250-fad8-3069-ae69-2723c03ecea6 | -2.98344 | -48.6063 | 2025-09-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a665cb64-4b2b-3fac-b96b-b553b2c4190e | -5.3731 | -42.62281 | 2025-09-02 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2fdc8810-1c8f-3464-9ff9-99bf6335d126 | -6.53664 | -42.9549 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a31f3c9-12b8-3356-bded-052b67136cb0 | -6.26193 | -42.60672 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0593cab3-e169-3016-8189-b381ecd0469a | -6.24996 | -42.42286 | 2025-09-02 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7fc01289-ca7f-3dad-8822-7c108eb5ef06 | -6.56933 | -43.71605 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0845ea9-bb98-34b6-b3c5-90d5a13b3710 | -6.54494 | -42.96684 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20c20c6b-8026-34ce-81dc-e360cefa6137 | -4.30914 | -48.09506 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8fc18614-63e9-338b-9e69-b17ec7badb58 | -4.47787 | -48.11478 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2f02c3f-d818-3732-9215-e0c62af4b103 | -3.8142 | -48.95639 | 2025-09-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7a3c2a2-ffc9-3aa8-835e-2d073efb7c4c | -6.17826 | -44.18908 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40994a83-6bc4-30e2-963b-e26294439daf | -5.86877 | -43.01213 | 2025-09-02 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7706930-0ee3-3942-8498-82586c2551e0 | -5.36979 | -42.62229 | 2025-09-02 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e0c455f1-d554-3024-8190-adf01a2c0d9d | -4.4814 | -48.11922 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81ac72c6-4005-3555-ab3e-bb76835f64b5 | -3.22809 | -47.12199 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6c4855-ddb7-3a65-9142-ccc2876f53ce | -6.19875 | -45.39877 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 554bd4ad-2556-3dac-afcc-38645d03928e | -3.22912 | -47.13435 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c1dc1f1-b39d-350e-8f51-569c1e424e27 | -6.16794 | -43.99602 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86c0bd82-c68b-3e79-9bb2-c87561eaa179 | -6.54218 | -42.96286 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 866a147d-5f8a-3697-b595-2f4884bdfa04 | -3.16678 | -49.47778 | 2025-09-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 263e31a6-21c1-36b7-b3c2-49f9728b9fb1 | -4.91881 | -43.1982 | 2025-09-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1fcf72c-9506-3f4b-a142-7b5f2d2c572f | -6.2553 | -42.60568 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 059eec4e-3311-37e7-84e1-72ac10f21c8b | -5.79779 | -43.84689 | 2025-09-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55995b43-a698-3dbc-8701-e5361144e41b | -5.78304 | -42.58471 | 2025-09-02 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ac8107d4-ef10-30a0-bd0e-7bdac2661160 | -6.49273 | -44.09079 | 2025-09-02 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331c1652-8d40-3bf4-86dc-88d328f4bdd2 | -6.57209 | -43.72007 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32c4f5c1-ef15-30c9-aad5-72008cc3036f | -6.27873 | -43.57718 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1cbec28-4133-387f-b2c5-3b9dde7234b2 | -4.30501 | -48.09438 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd18dfaf-af17-3dff-9cf1-2c9ee825668c | -6.18717 | -44.19775 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eeaf9e54-2e8e-398f-99ff-bfb221fda065 | -6.49608 | -44.06976 | 2025-09-02 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6948021e-ad4c-3f95-98ad-ce62d82ef17f | -6.73353 | -38.44738 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b124594-9458-3193-adc8-f1c515755917 | -4.06794 | -47.96112 | 2025-09-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a7663ae-ad0c-3e57-bc0f-82c9dc81442f | -5.96535 | -42.96045 | 2025-09-02 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9f1c3dfd-2032-3e4d-972e-170282e90abe | -6.22376 | -41.80869 | 2025-09-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7abf77ba-f610-3115-ae3f-0836961bce99 | -6.54163 | -42.96632 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d11d691-458e-3541-84fa-3ed890ebe506 | -5.50664 | -42.63668 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fb90e1e2-335d-33eb-8991-bea774fafae7 | -6.54385 | -42.97375 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43513033-4a06-3c4b-8460-dda770257fae | -5.77973 | -42.58419 | 2025-09-02 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ab14b39-413a-3fbc-939c-78402f853960 | -5.78392 | -43.84829 | 2025-09-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3563cd1-b375-3ccc-ac8c-1579fa08466d | -5.90798 | -46.62098 | 2025-09-02 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01dfcb31-f22d-3b7f-8507-4fb39e2b4975 | -6.30484 | -43.64865 | 2025-09-02 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README31.md)
