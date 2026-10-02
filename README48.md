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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56fa5809-02f1-37ce-b61e-8b8c9b0defcc | -11.65652 | -43.60539 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 2145b0ce-e3e8-3c49-b282-51cf335b0cff | -11.46685 | -43.43246 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce0cd4a2-f31d-3edc-a937-8e7a69576e64 | -11.73465 | -43.43699 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adc690d6-f020-3145-a08f-0c6f765a2c10 | -12.78476 | -45.17954 | 2026-10-02 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e38c25e8-666b-3030-80f3-dff5cd26ba36 | -11.67747 | -43.49636 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 894f3e81-fa76-367e-a205-fa93bc1c2224 | -10.71466 | -43.71645 | 2026-10-02 04:17:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd9bc37f-2126-35c6-960d-dd0f028564c4 | -11.2366 | -45.22862 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40c68edd-0a28-3651-ba16-bb6bba1e278e | -11.64987 | -43.6043 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 007436e7-bb22-3e6b-a29e-5b7d4fbc0f9c | -11.712 | -43.42963 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d328dd2c-95c6-3b32-9df7-4e6086a1d3ff | -11.74951 | -43.5768 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1c662709-51a2-3359-ab56-3eaabfa9b9d2 | -11.7606 | -43.57138 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23dd9e7e-b869-3c5d-99ee-114885160601 | -11.21491 | -44.84535 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c593f603-cd7b-3674-ba75-440d753744dc | -11.25058 | -45.2185 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9c8db8d-4717-3c24-9d20-340ee31cfea3 | -11.47454 | -43.44821 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ad9d3d9-7f4d-35cc-a3b5-86d41ff934ac | -11.30184 | -50.92327 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e2590e8-6d91-39c6-8f33-a036643c86fc | -11.40637 | -43.40813 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d513674-ecc0-3edf-ab0a-82e9eaaeb322 | -13.34538 | -43.85921 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be135ab9-b4e7-3584-886d-ffd274cf88b7 | -12.52605 | -43.09708 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dec27240-58f2-38d2-a692-74d39b5182cd | -11.25505 | -43.52431 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aeb3680-2682-3e1e-b860-8266cd6701a9 | -11.77114 | -43.56948 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e02ac08-9760-369b-bdd3-6cd8ae2a07ec | -16.89265 | -40.87558 | 2026-10-02 04:17:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e2cb912d-6a18-3542-b8f0-d62618ad83b0 | -14.91968 | -41.65482 | 2026-10-02 04:17:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4c0e862c-4fc6-3dfa-8326-6023cfadfa91 | -13.33875 | -43.8581 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2153cca8-2fdc-3308-b6da-0e11f038cb9b | -11.1453 | -44.61009 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a939ee92-3c6c-31b9-8386-4ba758f0c838 | -11.46022 | -43.43137 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50115d4b-2c1b-3ec5-800b-03c44a4034c6 | -12.52936 | -43.09762 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6eba59e-15fe-3e01-9645-349552ba8e70 | -17.44639 | -41.91397 | 2026-10-02 04:17:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 265ab81c-7fe5-30a4-bd4e-18f1a5e2b150 | -11.79989 | -43.58145 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| af34d86a-e811-3628-b08c-04eabdd5ed2e | -13.86412 | -43.63291 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 035ce418-d1bc-329f-b877-7c5a0e9fe6e0 | -10.90288 | -51.18316 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3e86916-0397-36f6-a252-5946f815d1f9 | -11.4696 | -43.43654 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 771ed121-44ef-3e75-978a-1c22163ba4b4 | -11.7628 | -43.57893 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0b5d8d63-9e35-385a-81bc-d1adf2d2ebc4 | -11.46192 | -43.42079 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c478a7a2-9eaa-36f4-9d8f-8353376ed5ac | -11.69145 | -43.60025 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58206c7d-34ad-3f4a-9f24-83fb78f585ab | -16.85693 | -40.57907 | 2026-10-02 04:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3ac5b460-ee80-3a90-851b-d7606c471e28 | -11.73409 | -43.44051 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e7f818c-7c4c-359d-9d55-fa9c78c47822 | -11.14035 | -44.59777 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0896f4e-c6f1-3946-8ce7-a8f587aa0898 | -11.46798 | -43.42542 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8129ea5a-9e6e-382d-ab83-7ece367da402 | -11.67427 | -43.60106 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 983549e8-b7a2-382c-82ea-c46cfba60a34 | -17.71312 | -39.75629 | 2026-10-02 04:17:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0f3c709-9b98-3886-a481-5c0828308e9d | -11.41413 | -43.40218 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21f62dc1-3e21-31f3-8955-f1140e681fdb | -11.13973 | -44.60148 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 58015107-6dbb-37d0-b107-4fc3fbe94890 | -11.4658 | -43.41782 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a77db07-cc18-3db3-bc7a-56893514fb58 | -11.74072 | -43.4416 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09a12019-b518-393b-89ee-b76cc53a9e2e | -18.33619 | -40.06178 | 2026-10-02 04:17:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d1d4439-0b4c-3997-9c52-212f3f16399a | -11.75342 | -43.44732 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42f14ba9-7c05-3cd1-ae46-a22bbd5caf03 | -14.339 | -44.7349 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ffa4ee2-7dc4-35d1-beff-5ec1a14c4bcb | -17.2241 | -41.19934 | 2026-10-02 04:17:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 991b42d0-34af-37ee-9014-9172687daa70 | -11.72527 | -43.43182 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45021f9c-b980-3bd0-b1d3-90066f8fe76c | -11.2496 | -45.21484 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5253d555-f454-36d6-89a6-d0d78711790b | -11.42133 | -43.39975 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 712d4d99-4c8b-3384-962e-1b26f0e41dcb | -11.76449 | -43.5684 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5edbcd0b-ae88-3435-b70c-9f4e39fe69c4 | -10.29918 | -44.65377 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1af6aaf1-40d3-3b1e-9e56-407f63afa412 | -11.13725 | -44.61643 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73b50ef4-5ede-3860-a8bc-927a2e215d00 | -11.30081 | -50.92887 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dafbc3d5-ec90-3814-9507-18847c604ead | -13.79655 | -45.25984 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d594e244-070b-318f-ac19-5dfa07bc4d0c | -11.18689 | -41.05111 | 2026-10-02 04:17:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 550ce0f5-ee19-3537-b80c-96299bece7f4 | -11.12948 | -44.61916 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d216f3b-2cdb-31dc-be64-a16a9a9a0662 | -11.24928 | -45.22622 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3d2a93b-b55a-386b-89cd-6e3c92ddf9b7 | -11.76838 | -43.56541 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07b5d8df-3cd7-34d8-bee0-3f1179648ba4 | -11.74347 | -43.44568 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e32c18-c726-3013-881d-2a45e67b3ad0 | -11.73684 | -43.44459 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e438afcf-0db6-3899-b09f-b06596395a44 | -13.39689 | -46.82173 | 2026-10-02 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3de4aaba-935c-3b5b-810c-1eb077ca9c86 | -11.74618 | -43.57625 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d9fd7154-f2f4-381f-8d92-68c68a47e205 | -11.72701 | -43.56985 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93879edf-a64c-3a70-9260-f6e221581453 | -13.33486 | -43.8611 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffef4ff6-1935-3a22-8cb4-0827512ed54e | -11.66762 | -43.59996 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19a2cb00-097d-3ee9-8c36-6a6daee97e25 | -11.13472 | -44.60849 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea600469-9ef4-3fee-a6f5-08ef788acd4c | -11.30674 | -50.92423 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b2e95fb-ab6e-370b-a443-63fb3223f295 | -9.87063 | -48.23174 | 2026-10-02 04:17:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 660d4769-d732-3e6f-9b2b-e0bac746064b | -12.99856 | -51.31794 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9df54c04-8da2-355d-8e65-7aa8b776a5ff | -11.24705 | -45.23035 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07f8be61-3a8b-36bf-9868-9b1c9d7a36c3 | -15.74595 | -43.65327 | 2026-10-02 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8917c55-9a20-39ab-b764-fadf228b667b | -13.34943 | -44.44159 | 2026-10-02 04:17:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed1007d5-51dc-366a-b5a4-ce5d66687896 | -10.89786 | -51.18218 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf46c292-dff5-32b9-b324-88b3d0f514d1 | -11.14933 | -44.60693 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 242d0722-59fe-375c-be86-00bdcb660946 | -17.42381 | -41.86211 | 2026-10-02 04:17:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85d58a9c-6b7d-338d-b3db-6fb5c097adca | -11.76393 | -43.57192 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3964b9c-aef2-3f14-b197-235a4c4f8739 | -11.74954 | -43.4503 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50589fca-bd9a-3673-b3ef-81dffabd21bb | -17.71243 | -39.76132 | 2026-10-02 04:17:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4178d739-5b05-33a5-b18d-83688702cdc8 | -11.78719 | -43.57564 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91d50147-1f60-3c2d-80a4-29da6427e3d1 | -13.38387 | -41.33109 | 2026-10-02 04:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 311c9f1a-a2ce-3104-b294-ad11c31a9eec | -10.3023 | -44.63487 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68b862da-ba3c-3d62-92e9-f96e1ca4fdf5 | -10.45804 | -47.11808 | 2026-10-02 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 854382cc-3c0a-38e1-a679-9fd4f99e723c | -11.75559 | -43.58139 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| feb6dc9f-b2ab-3cf3-aada-441c1d411672 | -11.40305 | -43.40759 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca1d7166-88a7-3412-9e01-7c99e102daa4 | -14.86943 | -40.70007 | 2026-10-02 04:17:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 48ae7abd-5d5e-3c73-875c-3769ccfa6917 | -13.33183 | -43.71202 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccaa5df5-0a3f-34e8-a257-2ab021347922 | -8.54706 | -54.56526 | 2026-10-02 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9fb7c35-81ed-3a4c-bca0-50d588fb4fdb | -11.68685 | -43.50153 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd18cbf6-8b42-34ba-9eb7-ed2877224c1e | -13.8663 | -43.64054 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 34759e82-14e6-35c0-a5d1-da13295e2468 | -11.23887 | -45.19316 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88b0c54d-06b1-3c58-b4f4-5ff1d7eb12e9 | -11.77891 | -43.56351 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c0f8e1a-2bd4-3fca-9a86-49cfad460cd7 | -12.99018 | -51.28162 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| b2342152-8cd9-34a6-bc4d-7cb7ecb2d8c3 | -11.70231 | -43.51134 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c05d141b-faf8-39bb-a1e2-8129dcd7eeae | -11.7319 | -43.43292 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e7bd22d-0575-3ff1-a35e-c614ca52522f | -11.46855 | -43.42189 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27e4261f-fb72-3575-8998-98bec8809669 | -13.38962 | -46.8202 | 2026-10-02 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c9a342d-71e0-34ce-be20-c210a3c52b35 | -13.39222 | -44.01326 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8566eca7-279a-36e9-a01c-fdba53f341dc | -16.99597 | -41.17993 | 2026-10-02 04:17:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README49.md)
