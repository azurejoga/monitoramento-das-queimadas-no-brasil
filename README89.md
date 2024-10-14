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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92e6855e-711e-33ee-87e1-10ec227d7f1d | -10.85331 | -51.06413 | 2024-10-14 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 092e76fa-d5aa-3174-911a-c050e35af626 | -10.79782 | -51.14301 | 2024-10-14 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6df12ef7-a670-3f16-b178-19e1fe251aef | -10.79393 | -51.14603 | 2024-10-14 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e0f0e72-81c7-3181-99a9-15ee522e442d | -10.54636 | -50.83751 | 2024-10-14 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 418b628e-6bce-3d83-8db1-518e7f37d491 | -10.54581 | -50.84109 | 2024-10-14 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce2b60c9-3a45-340e-b728-4bd3fbca8d14 | -10.43268 | -50.83047 | 2024-10-14 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33628840-ea59-387e-afa3-a0644648ff2e | -10.43214 | -50.83404 | 2024-10-14 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8c0c419-15e3-3a2d-a1a8-12ab2606e4b7 | -10.42878 | -50.83352 | 2024-10-14 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c543ef7-6f5e-3290-8816-f7ab9994760c | -10.41753 | -51.64648 | 2024-10-14 04:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfd85596-e277-31b4-8aac-0b5850ebb8bc | -9.81596 | -51.81913 | 2024-10-14 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a3d32a8-c041-31a7-aee0-974208ce94c2 | -9.49101 | -50.97748 | 2024-10-14 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99556457-1f77-3402-b20c-8d6ebe1743d5 | -9.43044 | -51.53883 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 082baccd-d629-3193-850b-14578cc8de9f | -11.40479 | -51.23808 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f03121e3-6306-3bdf-921d-4162356af389 | -11.402 | -51.23398 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36489d49-7ad9-309c-bf7e-6584f66b8d07 | -11.40144 | -51.23754 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dc0f485-e83c-35d6-b7c1-3a3501b7efe7 | -11.27006 | -51.34453 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1591adaf-e575-3616-8ee2-89252e1aec11 | -11.26964 | -51.43523 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 725f9080-954a-3b1e-bba5-e930d72a0c54 | -11.26001 | -51.32111 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74e4d089-7fdb-3d0d-b7ca-4769351ee1ce | -11.25667 | -51.32058 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d893cbf4-7ec9-306c-9e72-a4b0fd100851 | -11.25613 | -51.32413 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c371d4df-7159-3b3e-a51a-249bf7eac0d7 | -11.25279 | -51.3236 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d4d8f93-9d55-3647-91d2-879dac5346c2 | -11.24945 | -51.32307 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15c000a3-e3b8-314f-9f5b-7d1ffd5c2005 | -11.22832 | -51.32698 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b8f8899e-d5b1-3737-a646-e3870ac18d62 | -11.21721 | -51.33248 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 53ce466c-2bce-32e3-b5b7-8b0aac6b80cc | -12.97435 | -52.44805 | 2024-10-14 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df70c674-d50a-30dc-9b65-00cbb8c4383a | -16.75031 | -52.84158 | 2024-10-14 04:46:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd769b49-42ae-387a-9eb1-ec8d7b832d89 | -16.74975 | -52.8452 | 2024-10-14 04:46:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdc0f228-3299-3cc5-901f-0594036f7ac2 | -9.33832 | -52.84607 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b3218b3a-3037-39ed-9a7f-cac04aa491b3 | -9.33774 | -52.84971 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 378a0f03-fdf8-30ea-90f4-e93d7a19b054 | -9.33495 | -52.84549 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0fc3c4a4-dfb2-3825-865e-1a13011e10fe | -9.33437 | -52.84912 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| faf3f62f-35cb-3502-b526-c7fcf1401504 | -9.33158 | -52.84489 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 99edcf63-3e0c-340a-9d29-c4f0c8b7f4c3 | -9.33107 | -52.54701 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b6bb0ea-4970-3cac-a761-85513f418f68 | -9.32991 | -52.55421 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c4ddd68-8c31-39ce-9bac-7e9b6151f28e | -9.32771 | -52.54648 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f64c567-2e3d-3cb2-afc1-a4b45cd3c7c5 | -10.84627 | -52.40326 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4aa0fe-51fc-32fe-b347-48dc779ed719 | -10.84295 | -52.40272 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c81aceed-54a2-372b-bc20-8c40fefcbe7e | -10.84238 | -52.40625 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ffe0310-d1a2-3759-a672-ed88394db11d | -10.83905 | -52.40571 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 068edfea-7223-3cb9-b686-c2b4e1f9b176 | -10.69481 | -53.01406 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 933b769f-81b3-350c-9eff-b7148cec4d21 | -10.69424 | -53.01765 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5720765a-2e5e-3109-9b79-fad22e77c51f | -10.69087 | -53.0171 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e0efc70-b687-3748-a68f-8fb9e08f88c6 | -10.43871 | -52.91666 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 481c554c-2256-372e-8d53-4d4139b39976 | -10.43535 | -52.91611 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13ad9c7d-0539-3c3e-b7cc-17ba8851cc5f | -10.22312 | -52.68719 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09d427e5-e748-3e71-8a65-c6a04045f3b7 | -10.20787 | -52.33215 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcbecaea-dcc3-3233-be72-1fd7ebcab915 | -10.20566 | -52.32457 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0e9bb49-5723-3223-af24-8e317791feff | -10.2051 | -52.32809 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cc9d94d-4e7e-3356-b143-9054766fe579 | -10.20454 | -52.33161 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9f89292-2fca-3cd9-9720-e2057b42162e | -10.20177 | -52.32755 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 054d8362-bf0c-3547-b734-e6e1f7002385 | -10.15861 | -52.38943 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbf50a63-944e-35dc-aa39-99250638569a | -10.09272 | -53.09016 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd9b3b40-5876-3fd4-b7ed-410c5bbfc4f1 | -10.08934 | -53.08961 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e3e74d2-84aa-3c93-815b-f4ab39d6fbba | -10.08855 | -52.59237 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1e69adf-80e6-34f1-96e3-273f1305dad1 | -10.08521 | -52.59183 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2d7cb27-5595-3473-a234-9f5d68181436 | -10.08186 | -52.59129 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d4e1029-ab2f-3873-bacc-daa68debf096 | -9.88424 | -52.28025 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c32b57cc-ab6f-366d-9225-9a3dcbad8597 | -9.88091 | -52.27971 | 2024-10-14 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2092a8-ca06-3b96-9087-4c5fb78f19fb | -9.73346 | -52.84646 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5921325-f8a3-3fb5-ad3a-50b06ae151ae | -9.73288 | -52.85005 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a82c423b-5627-346b-aaec-e84351a69c3d | -9.7324 | -52.83156 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a551297-5309-349a-9989-1cc389a8a5d4 | -9.7323 | -52.85364 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7df683b2-9059-355c-8079-5b6403da2306 | -9.73182 | -52.83515 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf4f5235-d609-343f-ba2f-3e0b92a9aa05 | -9.73173 | -52.85722 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de132fb7-0331-3fe4-9de1-466c5378dcef | -9.73067 | -52.84232 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dd331a0-9008-3a23-9304-3438821603ec | -9.73009 | -52.8459 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 256e12f9-0a4d-3685-b8e2-2a93d603a953 | -9.72836 | -52.85668 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26c55d5f-0a6a-3e80-add9-951ee59c7c07 | -9.72799 | -52.81605 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f50c6f3f-a588-3e2b-9d4e-58fb7d85fcc6 | -9.72741 | -52.81964 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5f83d9d-63c3-3e02-8dbe-9bbd09bda162 | -9.72683 | -52.82325 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beb39c92-df84-3286-8d46-c8c81da69f1e | -9.72498 | -52.85617 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9f5965f-9d8c-391e-8d46-16d4438f8163 | -9.72463 | -52.81548 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f25b0c59-ebda-3393-acfb-ab48c9d05ee7 | -9.72405 | -52.81908 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eac23a1-81f5-3fad-b444-3ba88a04796a | -9.72394 | -52.84122 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54332bfd-3965-3bb4-9291-b6731642b6a4 | -9.72161 | -52.85566 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05ecb798-6526-3740-a399-83e65670ae75 | -9.72127 | -52.81491 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d48bde7-7bb1-352f-8b36-95daacd67af5 | -9.72103 | -52.85926 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a750dbf-15a0-3354-88d0-7a924b89f7a0 | -9.72045 | -52.86287 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a3d4a24-925e-3698-83c5-7be901a6467c | -9.71792 | -52.81432 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a71bf7cf-0721-3468-8662-24305fb9d2a9 | -9.71767 | -52.85868 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698d7374-cc80-37a0-ad65-31f7932a8c1c | -9.71709 | -52.86228 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d51aa1f0-7885-37d8-8bc5-560e6256ed30 | -9.71456 | -52.81374 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2184226a-c162-3efd-a9ab-ea00ffa68dfb | -9.71431 | -52.85809 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9d8cc15-463f-3798-9a88-4acd3505f345 | -9.71398 | -52.81731 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b323974a-3180-3ade-b5c6-b9fd63a035cc | -9.71373 | -52.86168 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8f8879f-8c80-3d94-8884-fa597b3dacba | -9.71094 | -52.85754 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcdeab5b-f6c1-3a96-aab4-5f53cd89f152 | -9.71062 | -52.81678 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fed26d87-24ad-30b8-8ff0-d708590564af | -9.71036 | -52.86115 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 595c85c1-26b6-3f0d-8afe-1e6393645a8d | -9.70815 | -52.85343 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a20ac062-d649-343e-8837-e9aff8d69943 | -9.70724 | -52.8163 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 639460ac-5eb9-321d-92b8-ce128dc4f66c | -9.70666 | -52.81987 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38b4bb11-9303-3490-8e17-9f0ab9c34e42 | -9.70608 | -52.82346 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6af83f21-a44f-354a-a8dc-3dedf71a2486 | -9.70271 | -52.82296 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd12bed4-7225-3b3b-95c2-64e5e5e8c9ce | -9.70213 | -52.82657 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d360ef1-1f68-3ce6-83ce-b2c561abd41a | -9.70037 | -52.83743 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b08e480-a95b-323a-b91f-c8afcc61cbae | -9.69875 | -52.82608 | 2024-10-14 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a2cef33-22f9-3a22-9e91-86e7ef5b2aa0 | -9.57999 | -53.255 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f6ab0f4-7a01-3b3e-b052-ca1fd83cf832 | -9.576 | -53.25811 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d09798c8-1153-3192-a31b-a1c6d7c77e27 | -9.56979 | -53.25327 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e3f485f-7990-3674-bd3b-dbd4ea136c9a | -9.43572 | -53.19776 | 2024-10-14 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README90.md)
