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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae05d1be-e0e6-3136-881c-c8d08b78bc50 | -6.8592 | -43.44867 | 2025-10-29 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a1166d5-f6a9-3c57-a3f0-67337e93385a | -6.17496 | -41.67329 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3e12ba66-fabf-3312-a71d-5cebf975e1a8 | -6.86357 | -43.44194 | 2025-10-29 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68eb83d0-fae1-3a7c-aa66-75a1003a42a9 | -8.05238 | -45.03061 | 2025-10-29 03:53:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 550d9eea-5ef3-3bb8-a027-228bd63a6f6c | -7.36201 | -47.62333 | 2025-10-29 03:53:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 28cb2e5c-bf0f-35bc-8ee2-89ca6b56bad0 | -7.93357 | -45.49821 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 962c611a-ccb9-3cc9-b8d0-c32adcb1bc38 | -7.90145 | -45.68375 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ab29a95-eece-3abc-abe9-fc1255244434 | -6.14647 | -41.57266 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e30b88d9-26e1-3e51-88bb-1cd8db1441c8 | -4.08243 | -42.92154 | 2025-10-29 03:53:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4700a817-e2aa-35c0-a9ee-9bf0655edf2a | -6.44055 | -42.36554 | 2025-10-29 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 060e9edd-e69d-368a-995e-3e2c3960bb19 | -2.82997 | -49.39563 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48e897a7-b989-3a58-aeb3-154a984c85a9 | -6.21741 | -41.82827 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ef9a3acf-6001-3958-8456-8117a3e4197e | -4.47571 | -43.43797 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9c1a04b8-b4ce-3c69-8aaf-1b7e6030c31a | -7.93016 | -45.51436 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a02f160b-4bf1-3e88-9af2-95b7e130bcb9 | -4.84708 | -47.53829 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6e7e674-1977-38b2-92f7-9bbec90c1c85 | -6.11602 | -41.7135 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e5a2bdfc-2af8-3cda-ae86-b51bb5fb53af | -4.48463 | -43.44254 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| d8491717-a43c-3196-809b-f8ef5b8a8a4e | -7.33978 | -42.47483 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 519d0768-3c75-36ae-81aa-630578abbc13 | -5.92502 | -38.31291 | 2025-10-29 03:53:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3eac7cf-5c43-3405-958e-417438650de6 | -5.39309 | -45.13301 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d502ba2a-59f2-3fbc-b8a1-c039830d632a | -7.89008 | -45.68977 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10464543-e959-3b3e-9104-020421f80ac4 | -7.31142 | -46.69661 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dbef2ed-a17a-3f17-a656-736f623c70f9 | -6.4603 | -43.55569 | 2025-10-29 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dfa770c7-4922-3f24-8800-e17ca21d54de | -4.75243 | -46.9772 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beefca3d-00e1-3ab8-9f5d-3bcf31f5070d | -5.06817 | -43.72004 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2fe4e3c9-7624-31e7-9ade-e7ca8eaebfe1 | -6.12839 | -41.84711 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 85e6fb69-ccc0-32c3-b49e-2aaeb433f1db | -6.13438 | -41.85709 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 4fa9a600-6ca2-3806-acac-2d98e7d932fd | -7.801 | -46.43811 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38b49937-2a51-3500-99ef-ce53580b4837 | -3.78841 | -45.59527 | 2025-10-29 03:53:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e8a5849-067d-342e-a24a-51d5b3062aaf | -6.46441 | -43.55626 | 2025-10-29 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d7e63ca-0e55-3b39-bbff-f783e0d4f01f | -6.5327 | -43.57118 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9231283-175a-3aa8-952f-aca33fbc2c0e | -7.06699 | -44.94332 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c90bffba-7224-3e94-abb0-bdafde5b32e7 | -6.63167 | -42.22269 | 2025-10-29 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d35f3fdf-dad7-33a5-9083-d836d297c566 | -7.74883 | -44.7203 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 126d5d7d-6f47-34b3-9591-d4d630cb9ef4 | -6.20679 | -43.26903 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2d21f16-e685-30b8-8ad9-db9d7ab37445 | -8.00513 | -46.20497 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3dce91cc-8d0c-3921-8ccc-e578d38b99a8 | -7.44561 | -39.2693 | 2025-10-29 03:53:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 479687da-2374-3beb-91b0-e859b68ef60b | -6.27127 | -41.81779 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96ecfc4e-0fce-3d22-9f96-e343751449ba | -5.35035 | -45.36363 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5faf5567-c464-312d-a472-ff716469e30d | -5.33399 | -45.43332 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2af3eb1-c96b-32e5-99de-9b5fa3baee09 | -7.93152 | -46.01152 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9b4e110e-d259-3776-bea5-f9327c8f8f34 | -5.65788 | -46.45413 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3e06802-c514-38d7-83f9-64af94b9f512 | -7.34431 | -42.47079 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8bf04cdf-d0a6-3ef7-8cf2-60c7654739d1 | -5.07466 | -47.1126 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49d2d946-8762-3849-8229-e4a2bf5fe7be | -2.63174 | -47.95976 | 2025-10-29 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2e11b43-af9d-310b-835b-47bfd73c26f2 | -5.2414 | -45.13536 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f600cac-5ce9-3be1-9417-997c3e63dce0 | -6.1321 | -41.70733 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 672cc3fb-c77f-3cd9-9064-62ad74aed608 | -7.43942 | -45.11524 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 791f47ec-22fd-3b09-974f-a629a1adfa2e | -5.47563 | -37.53246 | 2025-10-29 03:53:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc1e0a46-6aa1-37d4-907d-e99e5d75709b | -8.00434 | -46.20815 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a02bb0e4-4d2b-3aca-a305-18dccd2379f9 | -2.42678 | -49.29926 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 05976966-f6da-32b7-af8b-2a65368d2b2d | -2.42301 | -49.31081 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3915b751-5e39-35b6-b8ca-624c5811fbd7 | -4.08301 | -42.91797 | 2025-10-29 03:53:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54bb308d-9e71-371d-b378-b1caed2e8ed1 | -7.43861 | -45.11986 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3326438-1c1b-3eb7-b059-b43874299157 | -8.54229 | -45.68832 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51b8975f-f6d1-356a-918a-e63f32b7ea0e | -7.42419 | -41.86327 | 2025-10-29 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 819a15b0-226a-320e-aa6d-db6d293c87cb | -7.44892 | -39.26983 | 2025-10-29 03:53:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 973f631c-66e0-32b6-8ad8-b42eef8b9d93 | -2.53039 | -47.29963 | 2025-10-29 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f7a4707-ba0e-3457-b293-e74a8b4b6006 | -5.48536 | -46.44174 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36a4e419-afa0-3f0b-bf64-3e7254e3f832 | -7.59758 | -45.85564 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d371e945-9b32-3e47-a39a-b07513866ef1 | -4.75391 | -46.97534 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1ca7165-a314-32c8-80c8-25ec0996a0f0 | -5.43075 | -46.12291 | 2025-10-29 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6136098-307f-39dc-b36d-eed66585145d | -5.19302 | -45.62835 | 2025-10-29 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6221e561-60a6-3847-974f-f4ae00e0c016 | -3.81791 | -42.8006 | 2025-10-29 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0c316f5-be74-3f5b-8ac8-aae49a754fd8 | -7.86271 | -44.2383 | 2025-10-29 03:53:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff1d865-796a-3098-87ae-83e1311d1c9d | -8.21652 | -43.80845 | 2025-10-29 03:53:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92ff1871-3948-341a-857d-84b81dd4dcf4 | -6.61047 | -38.37229 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33c48979-cc62-3d16-9f6c-74f0117c6c93 | -4.08454 | -46.94595 | 2025-10-29 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5be372c8-5301-388b-8cd2-ada6fbcec7ec | -8.55146 | -45.68739 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d7c6401-cd1f-3f3f-9a4a-3326c470620b | -6.48744 | -42.24539 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3c47e1be-3e85-36e3-a197-ef3a988c34e7 | -6.14001 | -41.6818 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e84abcd3-2d69-3a6b-b77d-b1fd7f9c8b0d | -7.34355 | -42.47544 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 905c56b8-694c-39c7-bbb8-5f007343067d | -7.49792 | -47.04219 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cbd32c3-128d-3990-a544-bcf420cd383a | -6.29801 | -41.88556 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| a8b1ac26-06ba-3903-8789-1ff5bf2e5dec | -4.01005 | -43.2879 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c3a16d5-310d-3ebe-87c6-5a5e813ed9b1 | -6.28053 | -45.3153 | 2025-10-29 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b864ed4f-3e86-3112-8708-10e167423826 | -7.60354 | -43.57547 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8eb3aafc-bef7-3c84-a062-6d92964d45e2 | -7.49282 | -47.04132 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c15c3da-cc34-3890-bb5b-ce826dd6eaed | -6.17501 | -41.67468 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa3f223e-5028-3c3a-9fd0-eb44dd323cf6 | -5.6571 | -38.30915 | 2025-10-29 03:53:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e9671ed1-5481-37c2-8d1a-dd267b1785e8 | -6.10801 | -41.73943 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a7fc1d94-e9da-3c7c-8085-f78bc3dc9673 | -5.34511 | -46.8613 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 828782fa-d364-30a1-ae98-45aec9bed39f | -7.79995 | -46.4724 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a6dec196-76b1-3a92-9023-cc9bf18a6bcd | -7.95482 | -45.45746 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5a695aa9-4ab9-3a5a-b89b-eb175665b9d6 | -6.70395 | -38.20684 | 2025-10-29 03:53:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca74e4ef-4b08-39bd-9934-35505f8ed48b | -3.72267 | -41.56767 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f6c9e10c-d16b-36ed-83f4-2b1cd1b3e81a | -4.2944 | -44.48983 | 2025-10-29 03:53:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c7961b20-a4ea-33b2-9176-a07a6aec30ad | -6.12983 | -41.8382 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 37.0 |
| e50268c3-3b79-34d4-b890-a29e0070b9b6 | -6.49198 | -42.24128 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b2f98811-b098-3c20-961d-126d7e22340d | -3.89455 | -40.80281 | 2025-10-29 03:53:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2cc0c65f-9acb-3ba9-b222-89e4d4450f14 | -5.48027 | -46.44102 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 641c3900-8864-39b2-b356-0786ed08fb00 | -6.14234 | -41.71392 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d7101caf-89db-384f-b0fa-891ed4eec8f5 | -4.20294 | -50.08592 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55fda3c3-b432-34ac-8709-02857148de5b | -6.5407 | -46.76806 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3329ddd0-e94d-3dc5-a3e8-71a9bf7d3786 | -6.4912 | -42.24606 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5522cbd-2f46-3f89-89ed-3b9f33d37af2 | -5.99622 | -41.38597 | 2025-10-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e002f44f-615b-3f3c-b797-ef650702d55d | -6.13282 | -41.84321 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b2a973d-0c1a-366a-b758-0f29a57f2a37 | -8.54505 | -45.69921 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50f4a570-e0ce-39a0-8bf6-45f945c66768 | -7.90108 | -45.68139 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ec5e9bd-1f7c-30c2-a8ae-27436ac357b5 | -4.6628 | -46.39951 | 2025-10-29 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README13.md)
