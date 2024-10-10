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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 771645d9-9fc1-3ec6-8286-2fe5fba131c7 | -2.81481 | -51.59845 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78f6c65b-d81e-3556-b5e1-ebd52957b21e | -2.81173 | -51.59332 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdff39dc-6ba1-3cf8-9b4b-e4a2b40cb616 | -2.81081 | -51.59877 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 15eb6953-0f52-3b0e-89a5-d2f4976226c5 | -2.80989 | -51.59765 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d654cae9-1d66-3ba9-854b-25029d9dab34 | -2.63579 | -51.756 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aba5fa64-57a3-35f2-ad19-bc21253ac996 | -2.63079 | -51.75524 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdc7e19c-00b0-311d-b46a-5abdab1292cc | -2.58253 | -51.92278 | 2024-10-10 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c26a82-99e0-30d9-b604-7636e4e0518e | -3.55929 | -52.05013 | 2024-10-10 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efd80481-a716-3d5e-ab4d-01e3b277c8e3 | -3.92108 | -51.22182 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85340dbc-fbfe-34dc-a986-d263218b9688 | -3.84756 | -51.25584 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 988247dc-f444-3b59-a9c5-9e97c8c2dfbf | -3.84696 | -51.25362 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b595bc5-7072-32f9-b326-096f02936168 | -3.84671 | -51.26081 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12843671-3916-3d11-90a0-23300890ce51 | -3.84615 | -51.2586 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0550103f-fbd4-3c72-b7e8-bc8439a5bb57 | -3.84538 | -51.92884 | 2024-10-10 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb7289cd-81ca-3adf-bd0d-bb8fbae95acd | -3.84284 | -51.25503 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a51e525-5c54-33cd-8cc4-822a9fb9be51 | -3.84224 | -51.25282 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0a76bc0-1d12-3428-95c2-8716f5595cf5 | -3.84201 | -51.25994 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 643e9cc9-0338-3943-a36b-e64f17a5ded1 | -3.84144 | -51.25775 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb7e6cc7-1165-3f3f-bcaa-46a8306b4476 | -3.84044 | -51.92802 | 2024-10-10 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4245fe32-ea8e-3ea1-b4ad-ff31af0684cb | -3.84038 | -51.92587 | 2024-10-10 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7613a39-627a-3e31-af71-cde158280dea | -3.83812 | -51.25422 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0167dc7e-67ee-337d-9e9a-12bbaaec2f29 | -3.8373 | -51.25908 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d138be91-1cf2-322e-b72d-ac0c8bee8c4c | -3.68851 | -51.12337 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8b564f89-84e5-3697-ab25-751b08a21ccd | -3.68818 | -51.06778 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e12fc934-e495-38ae-89de-a31d40d4f1ab | -3.68768 | -51.12836 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6c0d5bc4-eeed-3144-898e-c9aadd719a9d | -3.68736 | -51.07265 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0eb0469b-96f1-3688-a17d-287ec202b66d | -3.68464 | -51.11771 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b9f93bda-7433-33f4-b217-12288ba7726d | -3.68381 | -51.12265 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 92215914-57e1-35ec-95f2-57900efb5c21 | -3.68349 | -51.06706 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aae136e1-f923-3613-9060-84605b2e7a8c | -3.68298 | -51.12765 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7122a2d6-526d-3882-bc6c-0c1583578dca | -3.68268 | -51.07192 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c7205c24-493d-356f-99f2-82188be03cc6 | -3.67911 | -51.12193 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 00c62e8c-63d6-333f-9de7-b996cdc44f6a | -4.44788 | -50.92358 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cf58e06-35cd-386a-ab61-3bf58cd42866 | -4.1652 | -51.04681 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1b3405b-8a0e-37e1-b0f7-5bea56e53f6a | -4.16059 | -51.04593 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17d68a43-cb21-314c-811c-d15d065c7f1c | -4.15982 | -51.0506 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 448fed1a-bd67-3d9f-81f2-856ca2dc5f3c | -4.15215 | -51.03942 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65fe0685-e6cc-3b31-8c5c-c1fef3d713c4 | -4.15139 | -51.04398 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 896cfb21-c9cf-3a28-b7d5-29e59877bf10 | -4.14256 | -51.09715 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b804357-30b6-3c62-824f-39f0525bd585 | -4.14181 | -51.1017 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8530fd0-19b5-300e-863e-8c344fcc9b40 | -4.1371 | -51.10128 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 674658e4-814f-34c6-952d-36234c146753 | -4.09381 | -51.02719 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24090acb-c2b3-3209-b3cc-6e3ad55ebb1e | -4.09286 | -51.02419 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 93dd0548-5a2f-3566-871a-b7cacc7eee87 | -4.09221 | -51.03705 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9c843f1-63fa-31a6-b6ec-1f5ac7cb77a0 | -4.09203 | -51.02909 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bd801819-657d-3ae3-960d-bc9fcdd451c2 | -4.09118 | -51.03404 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4bae6052-6560-3b05-a652-e754abf2a930 | -4.09 | -51.02139 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 915469ee-4a25-337e-9402-9a0ce896399e | -4.0892 | -51.02632 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4933754f-7af9-3384-b458-8e1724bc6b77 | -4.08909 | -51.01841 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e8498bb9-cfe7-3da4-9c36-e0f9cd4dcfec | -4.08839 | -51.03129 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 61122cc1-620b-3b65-a692-f2e6be563b17 | -4.08825 | -51.02332 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9987f03-e0cd-3de7-bef0-780117161844 | -4.08758 | -51.03629 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 82f600bb-0005-3d63-a760-c4766323a605 | -4.08741 | -51.02826 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3f112eb9-547e-3efc-9f84-9ee72004ee3a | -4.08656 | -51.03325 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 89e8aa50-4861-3c93-8a24-55aebf88a710 | -4.08572 | -51.03814 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f252619-b1f1-3049-ac24-5e0b96b08050 | -4.08538 | -51.02058 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 77e8fbd0-6a6d-3b40-ac67-0455951ad3fd | -4.08457 | -51.02555 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e6da5cb2-cc99-3a5c-ba29-23f20901c13f | -4.08376 | -51.03051 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29d3932f-ae6f-36cc-b3fa-516157bd0bec | -4.08297 | -51.03536 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 85f7eb86-0706-3f7a-b510-a4b745048a12 | -4.07992 | -51.02486 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f32dcd7a-3534-365c-998d-71e78499a350 | -4.07912 | -51.0298 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7be99acc-ed46-380d-8cbb-89302b1af86b | -4.06492 | -51.11661 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b200ce3b-f49d-3a78-8b48-f34b62fd1586 | -5.76148 | -51.44911 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d96d9b10-7f8b-3704-9eaa-bb0a5227dab1 | -5.76069 | -51.45385 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea41517b-42b7-3fba-96b4-b95ca39835be | -5.75684 | -51.44832 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7892304-045f-3332-a799-d51d8503bb5f | -5.6323 | -51.21061 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c88eaeee-0199-3cd4-b1ff-bb39150d6687 | -5.46735 | -51.35045 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a795531-e3b8-3346-b962-0f5adc2ddf14 | -5.76226 | -51.44438 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c9bcbbf-fbf4-39d9-831b-f544599d32c8 | -5.7599 | -51.45863 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4f667dd3-a6d1-313c-bf9e-f18559930dca | -5.75605 | -51.45309 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 070df424-175e-3b63-9d95-34cf0634629b | -5.63686 | -51.21141 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1e5153-f903-3bfa-9e97-5f724d7c8e45 | -5.07518 | -51.95763 | 2024-10-10 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61226c10-0f12-3bd2-a186-8218bd52a912 | -5.07032 | -51.95687 | 2024-10-10 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b55d93ca-3575-3999-8641-f54a401194ad | -1.65653 | -53.33932 | 2024-10-10 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00c7c15e-7c52-3932-b06a-227aa6e68617 | -1.65092 | -53.33826 | 2024-10-10 04:17:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1febdcc-1a44-35ed-bae5-f6b4699fe108 | -2.07643 | -52.02584 | 2024-10-10 04:17:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b327c34-b46b-3262-bec0-2cb2af5c027f | -2.07594 | -52.02886 | 2024-10-10 04:17:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6777187d-5904-3760-8fee-549ad9f8aae3 | -3.04479 | -53.04377 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08a1be32-aca2-37ca-acaf-51f32a9d48f2 | -3.03939 | -53.04283 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80ffa4d8-388e-3e49-a668-918e06064523 | -2.85895 | -52.90609 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4da17cac-438d-3ac1-91cc-31d71e37b2aa | -2.8584 | -52.90939 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56101d53-e530-3a98-927b-8d74779ce06a | -2.85786 | -52.91266 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79194043-a661-35f0-b8a2-e137fa45dc8e | -2.85357 | -52.90527 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1c40386-f2e1-37a6-9a90-58d4029b1a0e | -2.85303 | -52.90852 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e5a438b-75d9-3e8e-b21e-3d0bde94629b | -2.85248 | -52.91178 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27ab5faf-714a-3e0a-8960-be758cde6508 | -2.84859 | -52.93505 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4b1ba1a-ac59-303a-bfbd-18bdb723a5b5 | -2.84819 | -52.90443 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7513534d-6ab5-3210-a544-767d58d081be | -2.84801 | -52.93848 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3b13cf1-7898-339e-b5d6-c09a8a82085b | -2.84764 | -52.90771 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9de3f37f-037a-3f36-8990-fc53511309a8 | -2.84742 | -52.94204 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a7636bd6-f0f1-33e6-aa94-57de0a4c7a2b | -2.84709 | -52.91097 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a554203-bf77-34cd-a63e-200e7fc6c15e | -2.84319 | -52.93426 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 69adf4f1-7379-31a2-9437-0a119a6cc588 | -2.84263 | -52.93759 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28cf9f66-4b54-34ba-8ddb-0919276d837b | -2.84227 | -52.90677 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3bd39793-5391-3949-a022-a01ef595c1bb | -2.84204 | -52.94113 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fed4584b-e5e6-370e-8b45-1e37fcbf7264 | -2.84173 | -52.90997 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e65a0d9-fde2-3ae0-8a9a-77a350a8c6d4 | -2.84167 | -52.97639 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f6ba757-f0e0-3842-949b-9eb211542c25 | -2.84127 | -53.31788 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98a51e9a-8a2a-3282-8070-7cf09ed3bc79 | -2.84068 | -53.32149 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16c759d8-0f65-3c15-8c37-51837601ec84 | -2.83683 | -52.97218 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README68.md)
