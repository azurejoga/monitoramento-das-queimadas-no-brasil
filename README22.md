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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5adee483-5949-3b1b-906f-ccbea7aa8596 | -5.50389 | -42.62698 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2e278ae1-66c1-3f65-a1f9-e81c6c1ff142 | -8.02445 | -44.08392 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2853783-efee-3eab-adbd-37a2a025eb9d | -8.01739 | -44.10256 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cf55282-621f-3106-aafe-912ca98c602a | -9.18765 | -45.19381 | 2025-09-03 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06215928-b159-323c-9b9c-f64b5fd0b8e8 | -7.48804 | -44.80891 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e5071f4-64e4-37b7-925f-b83266ef18b9 | -6.40571 | -43.75073 | 2025-09-03 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24325a24-cbe5-3c3b-8f43-81c3bc46f880 | -7.92756 | -46.55074 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 722a2576-073c-35b9-9e96-27c5e8ffd1e6 | -6.69627 | -44.19126 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f9deef2-1327-322d-8e20-5cdfe019db82 | -6.72656 | -42.24548 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d812c5e2-ba41-3cc4-9c34-3c3eaf3576bd | -6.17179 | -43.30395 | 2025-09-03 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fdc49e4f-1856-3a92-a5f3-f14ce3335a0f | -6.03219 | -46.00821 | 2025-09-03 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4b2952c-1f57-31ae-a900-56be4f198723 | -6.7305 | -42.25251 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10c1237e-9246-343d-8f7b-46bbce3f7eee | -5.9003 | -43.3526 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7a8b209-bd38-385b-bd12-2f67765d62b7 | -5.70317 | -43.10492 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e9e8a39-9762-3129-ab31-c486fa7c6b7c | -3.35748 | -43.37597 | 2025-09-03 03:32:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc86afe5-ec7e-3a8b-8a6c-ebaabe884cf3 | -5.9376 | -43.02815 | 2025-09-03 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ab2591e5-1a2b-3ef0-be4b-8acbec4a192f | -6.9783 | -44.36725 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 503e0141-567c-345f-9280-2ecc849c776e | -8.02587 | -44.05817 | 2025-09-03 03:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e09c14d-1c04-3eb7-845c-22e78476c0b3 | -5.80151 | -43.22518 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9f354ea-9844-3c0e-a930-0962daeffc94 | -8.05701 | -45.37051 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0cf0b8cd-8d0e-352e-9978-11a0c6d7ef76 | -4.90252 | -43.21632 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8c36dbed-9ab8-3f9b-a2f9-569626d988be | -8.02169 | -44.11422 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca7214cc-8896-374e-b491-2d9d181dc035 | -5.79633 | -43.22378 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 715cd73e-b5bd-3955-beb6-7abca7e62bc3 | -4.89627 | -43.21509 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 554db1e1-b323-3a16-9af5-8ce9bb008f98 | -5.61255 | -45.01088 | 2025-09-03 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8badba68-da88-3fd1-ab32-4deae55460f2 | -6.73106 | -42.25347 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77b26424-9930-3eda-838a-72c908da027b | -8.04948 | -45.36914 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e411438c-67f9-3302-9d81-4deeb353c24f | -5.80067 | -43.2297 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d78f2da0-ce04-38c5-80f5-98245217bccb | -7.00204 | -43.25087 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f50e5b8-46c6-3661-bab8-2ca03172f18a | -8.01894 | -44.11388 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b99643b-3764-3d71-9850-a1dbb55f635a | -6.26822 | -44.49819 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09157b2f-d3a8-357a-839c-1f6465c48efb | -9.86348 | -44.68449 | 2025-09-03 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1e5e4d2-2c08-34b8-8354-cc58e2c4e24b | -7.93079 | -46.53969 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a0bbfbc-d115-323c-a095-608aaf10a797 | -7.93803 | -46.54117 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8e69b40-016b-3b27-b3de-9b8f7cd27f2b | -6.23967 | -42.62298 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c686fbfc-ee01-35e5-9b17-db0109938ac1 | -6.73464 | -42.26218 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d59ad50c-b763-3f4e-9cf4-7df4f03d0ded | -5.8071 | -43.23509 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54c7e269-fe3f-335e-863d-098003015299 | -6.27775 | -43.58493 | 2025-09-03 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b696a8eb-b93a-3131-865f-b76d4dd202c5 | -7.94062 | -46.5611 | 2025-09-03 03:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72fb3827-d0eb-3479-8539-fb142f1d2326 | -6.83709 | -44.77875 | 2025-09-03 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 199cf60d-8a86-3e5d-bd07-5cf27a68195b | -6.95823 | -42.97691 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bab4112f-821b-3981-9beb-b0a21189d10d | -6.24271 | -42.62185 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f01b142d-c7fb-3f3c-96c3-10ec36b8be65 | -8.02364 | -44.05297 | 2025-09-03 03:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4049ed70-9c12-3afb-9bef-03f5f4a8b523 | -6.78803 | -44.48724 | 2025-09-03 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ed83141-9c10-3c26-bb03-b5d7de58d333 | -6.27384 | -44.50488 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4e279f20-bf0b-3ef9-a124-6c3e3baa0fd7 | -9.62743 | -47.04589 | 2025-09-03 03:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4079345b-691c-3eaa-9cfb-1c88cbf98009 | -5.8907 | -43.35148 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e4748f6-4a13-3c01-8d50-05bc0b2c270b | -4.66664 | -41.95848 | 2025-09-03 03:32:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e4d3d555-b8a5-31b3-a12d-01a31c9c49bc | -8.0649 | -45.3662 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| df015ab8-8817-3718-897f-ca72f0e10c64 | -8.05039 | -45.3684 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ff52a2a-c5ea-3757-a727-3106d3ddeae2 | -7.94232 | -46.55738 | 2025-09-03 03:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a38ef946-0cd7-380f-9d6d-9a7039342626 | -5.53811 | -36.84866 | 2025-09-03 03:32:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2afe1c48-8730-31b7-bad6-80219a5e69a0 | -4.66737 | -41.95438 | 2025-09-03 03:32:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 525af7a4-eed9-3a4a-8310-4d23b40bb43b | -5.95323 | -44.28091 | 2025-09-03 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03b33d4f-e585-3163-bd39-1613171f0780 | -6.79748 | -44.09591 | 2025-09-03 03:32:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c0dfa07e-c6e8-3139-a8e6-d0ab32a12412 | -7.50065 | -45.34104 | 2025-09-03 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae9544c8-0fdf-3382-928d-a4343ceb02f0 | -5.441 | -42.90542 | 2025-09-03 03:32:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c5caf243-7bd8-349d-b843-89c46c145ece | -6.25035 | -42.59799 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 97f71492-1a74-3a0f-910e-c85402e47413 | -7.47569 | -44.83781 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1190397-e344-316f-9f3a-28625d41a145 | -8.89022 | -45.79394 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed69368c-963a-3291-b739-a6cca9a47207 | -8.07055 | -45.36928 | 2025-09-03 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad4a80c4-e0a4-3806-adb5-67ac407d4d61 | -7.1201 | -44.75322 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ced9f482-8add-3a8b-8f2c-a88669b4393d | -5.50166 | -42.62934 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 33db7c6d-e64b-3c18-bd1a-8aacc065136c | -7.9438 | -46.54997 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a192da6-3b59-3aa8-9662-805eed957f0c | -6.09408 | -43.28365 | 2025-09-03 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76b02923-fd26-3121-a51d-6fab81832257 | -6.47468 | -45.41333 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b372829b-029c-335a-ab11-4d8671b18b6c | -6.99871 | -43.2695 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3362ca74-cabe-36c3-bc5e-8e8fde1f2b57 | -7.01062 | -43.53293 | 2025-09-03 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8a1b82c-bd95-317c-8676-55ed71c654a5 | -8.43381 | -45.08683 | 2025-09-03 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e449001-12d6-326b-9537-50a5d63a69a6 | -4.67318 | -41.95542 | 2025-09-03 03:32:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d65fb8aa-2d5d-3eb8-8bd7-83440fa8658e | -5.88567 | -43.00726 | 2025-09-03 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 76dfefac-a007-3996-b66f-7880a52bfa4c | -6.35693 | -45.66186 | 2025-09-03 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ddd2f7d-0aec-370d-b942-e7964f5d64db | -9.63517 | -46.12505 | 2025-09-03 03:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86ba059c-b996-3872-b096-43569fa65335 | -6.2218 | -43.37749 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37b754d6-9d44-310c-9999-e59847f32281 | -6.78712 | -44.48493 | 2025-09-03 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5b9441a-d103-3967-9ca8-669f07dd286f | -5.92818 | -43.35756 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38b97445-20a7-3f68-8792-baeced3dd594 | -7.48575 | -44.82096 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fdcd88aa-d8f8-3eb3-8485-6d0f0fd17920 | -6.35162 | -45.67119 | 2025-09-03 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ac02a1-29a9-35f1-857b-ea2c8d7aa6bc | -5.8865 | -43.00266 | 2025-09-03 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5cec2e42-0d0e-3071-ae40-e246231947b9 | -6.58353 | -44.58404 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88af4e0c-7e5d-38e7-ac23-ad5a567125b1 | -7.48018 | -44.81417 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d859863-4fd2-3b4c-b8a3-7e96f2b5a438 | -6.17011 | -43.31321 | 2025-09-03 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 7285e217-394d-3537-b4b9-f2fb19ee1699 | -8.01644 | -44.10751 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0df7a8d2-7467-3e6a-a58f-0de30fd17648 | -8.88897 | -45.80028 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28f6c179-0be0-3179-9f76-0bb827073ddc | -5.8079 | -43.23054 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fe7d790c-ade2-37d6-a435-0093e91b4d53 | -6.24558 | -42.62408 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5d7716cb-2916-3f00-a316-e4c8c1e1f1ca | -9.62831 | -46.12347 | 2025-09-03 03:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb32caeb-d292-3407-b4e1-e0eb80e0ad5f | -5.93678 | -43.0326 | 2025-09-03 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 927391a3-7e6e-362a-8375-f205295043c3 | -5.6424 | -43.68047 | 2025-09-03 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 534987e3-d443-3556-9981-53e34c65bf10 | -5.53751 | -36.85226 | 2025-09-03 03:32:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6fde5377-5e68-319c-b493-08df065df00a | -9.61397 | -40.61321 | 2025-09-03 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe3308fd-97e9-356c-a904-d03a77973d6c | -6.19517 | -43.34835 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b7de023-c04c-3bef-86d4-83d9eeabbd3a | -8.01985 | -44.10892 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6858330-5a7e-392d-9472-0caadd530c64 | -6.69454 | -44.18337 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df90bb2a-49df-3ce1-a46f-318abbb9ad0c | -5.9379 | -43.03196 | 2025-09-03 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f23380c-f94f-3ca9-9072-4ad84080736b | -5.53344 | -36.85158 | 2025-09-03 03:32:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 88bd377f-3515-35b3-94ab-a2b1a4ec720d | -6.17095 | -43.30858 | 2025-09-03 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9d53f89f-5621-3cc0-920f-54a7413b7eb7 | -5.68828 | -45.93895 | 2025-09-03 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e643c690-13df-308e-9a71-c970ffb4d782 | -6.47861 | -45.41922 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d1e70508-af61-32fb-92c5-99e3d9af2c7b | -6.47294 | -45.41089 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README23.md)
