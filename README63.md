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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 496c39d8-c47b-32ba-9471-9323c8458fe9 | -11.94315 | -64.88314 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7114301-b4ab-3f9c-a597-ccf79105b263 | -11.94165 | -64.87003 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fb64418-acb5-3960-96df-3e0ea3324c76 | -11.94096 | -64.87418 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c347845a-5256-3aed-a678-c8fcf50107f6 | -11.94027 | -64.87833 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6d5e353-739c-30bd-8abc-7a7a616eb597 | -11.93958 | -64.88251 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8e0c0dc-27bf-3da8-b9a1-38d06711d4ba | -11.93899 | -64.90811 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7749bcd-c278-3441-9f94-1012972edb35 | -11.93809 | -64.86938 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 258763e2-daa8-3dc9-8988-c7c5d778747a | -11.9367 | -64.8777 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5de5c3b-dc27-3024-b3f8-92ad34de8f14 | -11.93025 | -64.87231 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0924db88-d1da-3d2e-b22e-7afe9fcd64ca | -11.92668 | -64.87168 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f15456f5-0ecc-30d7-ae3d-63c80237172c | -11.91883 | -64.87462 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66e6ca83-38d6-3208-94d4-34f3a6915a2c | -11.90342 | -64.96648 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09cca5c8-88ec-332d-bf63-9eb7693e7607 | -11.89328 | -64.93895 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50da277f-ebd7-35e8-8b01-0d4cecab063c | -11.89252 | -64.9216 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f270364e-9db7-3166-8d34-458806b06295 | -11.88752 | -64.92934 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 944a66d6-b588-3fe1-8a74-13b84a919f0d | -11.86897 | -64.99529 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63b11640-10db-3805-9c14-8ca6feaa3574 | -11.83189 | -64.85235 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4da5fa89-400e-3f6f-a861-0a58f166dac6 | -11.81839 | -64.86716 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d076b8bd-ef41-3f9b-8622-4ba9362a8a99 | -11.74658 | -64.82108 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb01d579-c804-3035-8e1c-cc59b1ad9ac4 | -11.74576 | -64.80391 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90a1007a-e88d-3065-8344-38484d10bcc5 | -11.74219 | -64.80329 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57f95c0b-05fe-3f7b-a86c-e976baf927f6 | -11.72962 | -64.9771 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ce26df3-b289-3829-aca9-5ccb908659b9 | -11.72055 | -65.22662 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6bdcc133-fb57-3b05-b38c-39cf7762b1b2 | -11.7169 | -65.226 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d24eef78-3971-3268-8bb2-f3e6e284755b | -11.71326 | -65.22537 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 80f6eb05-0e66-3714-9ee1-8fc92d0b4355 | -11.7111 | -65.21606 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad6eb303-7fa3-3d77-9639-d1ceed0d9123 | -11.70961 | -65.22473 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f508bb91-bb61-351e-8ed0-069a96553b94 | -11.70448 | -65.2328 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e813ef0-f0f7-3936-887a-3979edbe3411 | -11.70373 | -65.23713 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6793be96-4256-3be6-b45c-2453d8dbd091 | -11.69718 | -65.23154 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 667e6a0c-9a4c-33f9-a92d-3ea74b28d157 | -11.69651 | -65.21356 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90398dc2-d891-3bca-82c5-3ae219db887b | -11.69643 | -65.23588 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8731d1c5-b9d1-31b3-a8c0-8dbc1e1feb57 | -11.69569 | -65.24023 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4045228-59a3-3b40-a6c2-8d3e08f105c0 | -11.69428 | -65.22657 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ef52add-6d0e-3926-bc13-58968cbfd6b0 | -11.69263 | -65.21368 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78c273ab-a082-3749-bb50-07dbfd97f7b8 | -11.69212 | -65.21726 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 048f5079-07e5-3094-a18b-b51ee578313d | -11.69204 | -65.23959 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4441b4c6-9ae7-3047-a0b6-ae7671d010ca | -11.68971 | -65.20869 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8de68c6-504b-3c4b-a865-81a6ef060317 | -11.68922 | -65.21229 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c4d6546-cc25-3e08-a62f-3ef830c7a1b3 | -11.68848 | -65.21663 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b3a2cf4-2a24-3fa6-b1e3-79f4ff3a92e2 | -11.68838 | -65.23898 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fa99fb0-588f-3161-bd5f-36c522918f39 | -11.68827 | -65.21738 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35025b8b-9165-3b75-bb60-c1f1fd12ca5d | -11.95651 | -64.84695 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4865f9da-bc61-3389-a87c-92236c174a6d | -11.95236 | -64.87196 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbc6d000-cb7c-3937-b68f-a37e06f213d3 | -11.94453 | -64.87482 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5aa71358-a89b-3957-938f-79712a377df0 | -11.94384 | -64.87897 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c4fc8cc-efdb-32fb-b37d-f012aa14a3f6 | -11.94234 | -64.86589 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db6b15eb-245e-3718-a125-2649e1904a05 | -11.93739 | -64.87354 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c364d3b3-a639-3040-a9ae-437ca9793785 | -11.936 | -64.88189 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e53efa9-1d6a-3881-a0ae-9e5e5848a351 | -11.9353 | -64.88608 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 821577db-ea87-3aca-8a68-453addf096c2 | -11.93451 | -64.86877 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 937401f0-ad87-36f5-8914-203acabb3312 | -11.93382 | -64.87292 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d5f564-a75f-3b49-be60-a59201f82b75 | -11.93313 | -64.87708 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f601f6fa-241a-30e2-9478-d5190152d9f6 | -11.93173 | -64.88545 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f659f88-4945-33c6-9689-51d58b351866 | -11.91246 | -64.89066 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f227ff8-b861-33a6-8dde-29cdc177f470 | -11.89687 | -64.93957 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d695878f-b06f-3c48-95aa-85d136e0b188 | -11.89322 | -64.91743 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d1235e2-6ca6-3ab8-aacb-fe28f335126f | -11.8904 | -64.93414 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e897afc-a0a1-3aad-95ac-8693a2521d74 | -11.88894 | -64.92098 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07d76ecc-07f9-3ce3-9d90-07ef58daeb9d | -11.88823 | -64.92516 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f12d78b-d492-320a-9942-2110e274fe4b | -11.88682 | -64.93353 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab16ca86-b910-3390-a30e-cbe049bb21f0 | -11.86825 | -64.99953 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85a9fd43-4bfb-3d51-a764-3e6c8d6bf60b | -11.83478 | -64.85712 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7690b3a-abd2-3412-a256-a453292dcecb | -11.75084 | -64.81754 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fc31375-3eea-31f6-95e8-cedb01ff6c7f | -11.74796 | -64.81278 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5824c43c-40ad-3a50-86fb-7a87bdaf6a45 | -11.73367 | -64.81033 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac0368a8-8ab7-3608-814d-f5462b869e07 | -11.72878 | -64.97316 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f675e47-2834-3327-b4b9-22e6ab619953 | -11.91456 | -64.87817 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 920a1170-e1ab-39a4-8fbf-cfafc44d8f84 | -11.91176 | -64.89482 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 520fe6f5-e1ba-34e4-aa2c-23e34103bc9a | -11.89681 | -64.91804 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 34615b47-ee4b-3a98-8f73-b1d5eb64f1eb | -11.8312 | -64.8565 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ea288b6-983e-308c-8710-0ea3da9e358e | -11.75153 | -64.81341 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcec4a89-b2a4-3f3f-a33d-d8573b38dab4 | -11.74864 | -64.80865 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 620c9379-bcac-3668-b68b-8051efe35baf | -11.74507 | -64.80804 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6015684-9b4e-38fe-a983-6bdb70031abb | -11.73862 | -64.80267 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f416a91-29fe-376c-bbe7-d3fef66106bb | -11.73793 | -64.80681 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8459b590-4455-3c38-afe1-8873e64511cc | -11.73436 | -64.80619 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3aab3aad-d1d8-3dac-9359-0349047b34ca | -11.72808 | -64.97741 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72b48e7c-7a09-39bd-9a87-81361d8f7599 | -11.72675 | -64.97225 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6e27f4f-79d2-3c58-b2b1-c9353319c542 | -11.72602 | -64.97648 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46dcc56b-d2ec-3999-b74d-5ef192312318 | -11.66446 | -64.8284 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e64b91e-8cea-3c35-b478-4a003458d735 | -11.65801 | -64.82301 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3108980-14ac-37cd-88cd-578433fe55f3 | -11.65372 | -64.82657 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5c778d7-e1d1-36cd-8849-09f37cc39eb2 | -11.71981 | -65.23097 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 605611a9-f64c-3987-acc1-fb1d7782561e | -11.71765 | -65.22164 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0a46c44-c7a8-3e30-bcd2-5a4dd489d341 | -11.70887 | -65.2291 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9fb295e9-ef03-37dd-94bd-18ec01210674 | -11.70745 | -65.21542 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcb67731-22c3-3e91-962d-cd6d64ed9cea | -11.70738 | -65.23775 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 634d252f-8082-30b0-b406-0320ddb84616 | -11.70596 | -65.22411 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abc7e558-9c8e-3d00-a9eb-d6e07523c02c | -11.70522 | -65.22846 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dab0e7a3-bfc3-385b-a430-340ad7d629a1 | -11.70455 | -65.21047 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cad7cb6f-ff09-3a8c-8dd1-ececc8ad8d02 | -11.7038 | -65.21481 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1db3e68f-8e06-3712-ae37-d5a319ae20db | -11.70232 | -65.22348 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55553f44-dc49-34f0-b20c-a18205da15bc | -11.70157 | -65.22784 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ee9dce6-eb3a-3e59-9a76-ff2936fc4bc8 | -11.70083 | -65.23217 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 751d6a3e-d91a-3ed1-a9a7-5c6498485ea8 | -11.70008 | -65.2365 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d32da55f-10bb-3378-81a2-1076526470e9 | -11.69867 | -65.22286 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16eabbc2-392b-3f36-ad94-ee519278f4a1 | -11.69792 | -65.2272 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 883c4611-479f-3ccb-94f4-8e942ac6f4b4 | -11.69336 | -65.20934 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9db0dc7a-72cc-3539-a912-68ea0aed3ac8 | -11.69287 | -65.21293 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README64.md)
