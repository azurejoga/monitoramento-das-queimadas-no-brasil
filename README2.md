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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22851fb4-e498-368a-8fd2-9e9f46a3abb6 | -11.80006 | -43.63153 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1c91e5a-02e0-3329-9724-dd114fb689b3 | -11.80063 | -43.62767 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a8dd50d-ba41-38f2-80bf-3b290aeebfbd | -11.60623 | -55.32484 | 2026-04-11 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56980b23-62a8-3dba-8a98-73403f5afd3d | -11.79718 | -43.62713 | 2026-04-11 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aaad00a3-7139-3d22-ae8b-047e218f6818 | -15.28162 | -43.07209 | 2026-04-11 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6eb2421-3c0c-3c7e-bc58-de4cf71410e8 | -18.95494 | -53.45286 | 2026-04-11 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c646b272-ed29-3f72-a1a3-da789703e14b | -19.97803 | -44.85431 | 2026-04-11 04:23:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01eafaa9-1900-35ce-92ee-3e98121c9459 | -15.28529 | -43.07262 | 2026-04-11 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1fb04b35-be60-3dfe-a0ad-8af4c8b32017 | -13.24583 | -53.29174 | 2026-04-11 04:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 178a0cc4-4ff2-3e68-8085-c340f9c56a20 | -13.24493 | -53.29654 | 2026-04-11 04:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87b57cb3-ad33-3ca2-a87e-ff7f3a0f8c8e | -17.91058 | -54.12379 | 2026-04-11 04:23:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef8f9409-a2f1-3274-a496-9b44d4267a6f | -15.28592 | -43.06819 | 2026-04-11 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 26ad9d42-4b2a-3e8c-9e63-dfa7ea8cc64c | -14.76785 | -47.15619 | 2026-04-11 04:23:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d5924e8-b9d9-3db2-a5d3-9bdc722eed0d | -18.7844 | -51.9269 | 2026-04-11 04:23:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 850ce3d5-0a2c-33ca-ab5c-57f8611b06d2 | -15.28225 | -43.06766 | 2026-04-11 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ca8940d-949b-393b-a1a3-1b04e5300644 | -20.9149 | -49.52787 | 2026-04-11 04:25:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d9e11ea-c30c-3421-a69e-6cf9cfcb660b | -25.83291 | -49.27975 | 2026-04-11 04:25:00 | NOAA-21 | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f212f4ab-3ace-350a-83aa-1f417082a6d9 | -21.49831 | -47.17856 | 2026-04-11 04:25:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf3d1919-e4c3-3a4f-a189-a0f7f9010699 | -21.27585 | -54.41089 | 2026-04-11 04:25:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2049c0a-779d-3a04-be68-6f65fc43e59f | -21.36928 | -53.85378 | 2026-04-11 04:25:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa3c05c1-0f00-36e5-99cc-5ab151c75d1b | -22.87829 | -48.6494 | 2026-04-11 04:25:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f17d33d-311d-3853-af96-d98d55f3306f | -21.04682 | -54.30511 | 2026-04-11 04:25:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a11d3131-6865-31fa-a76f-cb924d5a3b3b | -21.27418 | -54.41378 | 2026-04-11 04:25:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5538ddef-c154-3995-9248-865c3a05c031 | -20.14134 | -52.41262 | 2026-04-11 04:25:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91d1afa9-33df-348e-86f9-d0743926771d | -21.05105 | -54.30606 | 2026-04-11 04:25:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dafeb661-2e25-3cec-bd7b-79386c50234c | -21.71866 | -48.43382 | 2026-04-11 04:25:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 523f4559-7395-3773-8640-571ec51159f3 | -11.60238 | -55.32512 | 2026-04-11 04:53:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0554e3c0-b316-3e29-a97f-2bf8754ede3f | -13.24538 | -53.29484 | 2026-04-11 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 56188447-e2af-3a69-9caf-0dd5df796e2c | -11.98816 | -47.14953 | 2026-04-11 04:53:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b8601b4-48b5-3944-8331-e6ba0a54e78e | -12.95141 | -51.62784 | 2026-04-11 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb87d863-be4f-3c6f-81c5-036af1c62a41 | -11.6043 | -55.32669 | 2026-04-11 04:53:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b2064bc-79b0-3ced-822b-cedbb6fcdeec | -11.93025 | -58.07344 | 2026-04-11 04:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71522dd8-eda0-3a5a-944f-07aac324b1e1 | -11.60597 | -55.32574 | 2026-04-11 04:53:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d5b1777-95e8-330d-b1ea-16482c8de4fb | -15.28431 | -43.07034 | 2026-04-11 04:53:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7d7cdd65-5b49-3975-be3f-88e715d65d25 | -13.24596 | -53.29128 | 2026-04-11 04:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0825603a-7cdd-357d-8d5f-266a401c39c6 | -6.86925 | -50.37819 | 2026-04-11 04:53:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5902552-3cd0-39fc-8a15-18b2d0eb2f87 | -11.93513 | -58.07036 | 2026-04-11 04:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2561976e-7862-359a-9875-46e1a1db6403 | -21.05103 | -54.30425 | 2026-04-11 04:55:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33bc6c9b-07ad-374d-a0b9-8477e94a1475 | -20.16133 | -56.35043 | 2026-04-11 04:55:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 761312dc-4405-3d21-812a-e6b2cad5a814 | -21.3682 | -53.85476 | 2026-04-11 04:55:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac58f2f1-759b-3505-aa0a-63a2aec62a5f | -15.28167 | -43.07336 | 2026-04-11 04:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dfb3f93b-8459-3c84-92f0-3d3a12232c54 | -21.27453 | -54.41198 | 2026-04-11 04:55:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3da7ad51-95b7-3c98-bbd8-0d59d589fd2d | -20.14141 | -56.34253 | 2026-04-11 04:55:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 635739cd-c475-3806-95f1-d724533c5c17 | -18.95465 | -53.45207 | 2026-04-11 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fe6cf57-cfc7-358e-a84c-9c1296942a6f | -21.0477 | -54.30366 | 2026-04-11 04:55:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 434dc7e3-b26c-33e4-94ab-d002f3cda408 | -15.28209 | -43.06955 | 2026-04-11 04:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2e105544-3e96-3795-b5a5-2b05ce8cd250 | -20.13976 | -52.41382 | 2026-04-11 04:55:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d57090a-2c84-3572-bf27-99e9df153aa6 | -22.87902 | -48.64705 | 2026-04-11 04:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6ebbe7b-cbce-3985-8fbe-321752b798c8 | -22.87851 | -48.65137 | 2026-04-11 04:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56f9896a-5989-3a80-aa26-b13e0e734965 | -21.17262 | -56.84739 | 2026-04-11 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bbf8ba8-7bdc-37d9-a53c-40581ca30ffc | 3.69457 | -61.51553 | 2026-04-11 05:10:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb907574-ff00-37d8-a80c-ad8fa451e2a8 | 2.90921 | -60.36702 | 2026-04-11 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401cc4f5-2d22-3925-b37e-e4d63285bb10 | 1.8293 | -60.87069 | 2026-04-11 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 935e3af0-3799-3e23-be15-0c124b0dc681 | 2.90517 | -60.36763 | 2026-04-11 05:10:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e808fbb-91dd-3a25-b5b7-6b4f99a2f1b8 | 2.21204 | -61.08602 | 2026-04-11 05:10:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aae2d24c-e1f3-398c-b38f-ae6a80be0274 | 1.82986 | -60.87436 | 2026-04-11 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 954e5745-5a2d-368b-b64b-2d0e41a77136 | -6.86872 | -50.3782 | 2026-04-11 05:12:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6ee91af-b6fd-315b-b5c1-244af5360ad0 | -13.79637 | -57.33224 | 2026-04-11 05:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef791ae8-fccb-3400-9594-a59b04f8fe91 | -13.24368 | -53.29546 | 2026-04-11 05:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cf8a436-fa23-3e73-8829-19a673fbf514 | -11.93183 | -58.07368 | 2026-04-11 05:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c310ed65-970b-3c30-9cb7-6402f2ab435d | -13.2442 | -53.29154 | 2026-04-11 05:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9247403-8e52-3cca-b056-3539bf5fe82b | -11.60308 | -55.32416 | 2026-04-11 05:14:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034b0b02-66a7-31cc-bf7b-6ab00636c11f | -11.60608 | -55.32897 | 2026-04-11 05:14:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0156664b-926f-3c03-8be9-339ae2c1f848 | -11.93238 | -58.07014 | 2026-04-11 05:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66d4accd-3eb6-3444-b4dd-bac8a62e6ea9 | -11.34243 | -55.29649 | 2026-04-11 05:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84d1a8e5-ff85-313b-a646-ea6dedc58984 | -16.59849 | -58.21747 | 2026-04-11 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 5401e51f-24cd-339f-9f74-7000a424bc74 | -16.59511 | -58.21693 | 2026-04-11 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 12f7d569-6ece-3105-a800-e11b0f057b1d | -20.16068 | -56.35068 | 2026-04-11 05:16:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df938295-5444-35cd-9f72-99a5e6546d9d | -22.87633 | -48.64782 | 2026-04-11 05:18:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1df33e09-a91a-3ec9-9c8e-0a20e745791d | -22.87592 | -48.6533 | 2026-04-11 05:18:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91e5c16d-6227-3be4-bef3-12dcc3e47891 | 3.99761 | -60.97275 | 2026-04-11 05:57:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 106cb31c-2ec1-30ea-8b52-21849a67c0a9 | 3.9953 | -60.97481 | 2026-04-11 05:57:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84f30251-9fcb-3ecd-87de-bb982a3bc2c5 | 1.82793 | -60.87175 | 2026-04-11 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15f30eaf-a48a-3a97-b5c7-24678ffb4ca1 | 2.37496 | -60.90767 | 2026-04-11 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ba23162-33b6-3088-9748-91c7d0e737ff | 3.69402 | -61.51181 | 2026-04-11 05:59:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 311c64cd-d4e8-35de-89a2-6e7ee62c5aff | -6.5631 | -51.1126 | 2026-04-11 08:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 32350c22-a633-38c1-b764-dd2c764a7bb0 | -6.51538 | -35.50051 | 2026-04-11 11:23:00 | TERRA_M-M | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fba8d211-ae34-3d2a-93da-3c1f03c89c42 | -11.39465 | -39.53582 | 2026-04-11 11:25:00 | TERRA_M-M | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 726707b8-219f-35f2-bf9d-4d07827a8079 | -11.39595 | -39.52683 | 2026-04-11 11:25:00 | TERRA_M-M | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |


