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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c527778c-b5c2-3912-9a34-ffa59be024c1 | -6.979 | -45.00549 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1bc6f120-7474-3d98-b917-c737830a4e67 | -6.96365 | -44.69463 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 677f450f-68ff-357b-87e2-32000ef62f27 | -6.93159 | -45.07542 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a5c9aae-cf5c-3bd4-8ed9-c57a2f084c50 | -6.9256 | -44.2601 | 2024-10-25 16:52:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d20dc7d-4358-3439-8e04-6e3b6bbd0b6c | -6.88733 | -44.32208 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 631edba7-16aa-39a3-bbdc-d17b6e726f35 | -6.88672 | -44.83242 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78bcbfee-7338-3214-bcb0-eafbc9d45060 | -6.82749 | -44.76804 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dd9c626c-b6a8-3fdf-9654-ef6135e1badb | -6.78384 | -44.71216 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5c7e1be5-7f00-3ffd-89b7-f361c756b769 | -6.77963 | -44.71275 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 062cd00c-a523-31a9-b89e-67d81265b6d3 | -6.69842 | -44.30586 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 326daf72-efb6-377c-ad73-3b6b2724fcaa | -9.10818 | -45.49988 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 96521013-76dd-3d04-af7a-975d87cb258e | -8.62681 | -45.2916 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| c5356825-e7c2-3249-baeb-0eba316fe2f6 | -8.62579 | -45.3583 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 87791d28-99fc-3adc-9a53-87d7bb76d873 | -8.61813 | -45.28799 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| bd59ac9d-682e-34be-a608-62438777ae2b | -9.01065 | -44.95977 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 570aa800-3ceb-3c51-b07c-81ad635d314d | -9.01003 | -44.95604 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 889f4ee9-f5b3-35ec-a1e1-9e8a6bd4eeba | -9.00209 | -44.95759 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 819a6e2f-d3e2-3f3c-bea3-12ce0a4096e3 | -9.00088 | -44.95034 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ed4b482-c23a-3053-b32f-7a2f2e006b75 | -8.99691 | -44.95118 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 670b61f1-71aa-3c99-b031-5033707b6ad4 | -8.96966 | -44.98412 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6fb6db8e-5700-3521-a263-c40828ec6ce6 | -8.96568 | -44.9848 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5dffde86-1e25-3a8c-8db9-e9e1195d0b25 | -8.9555 | -44.99722 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1799ec94-805c-33c9-ae72-28e94bb0077c | -8.81117 | -44.91885 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 81c39e8d-fe89-3e04-88ae-c73a1944083f | -8.81058 | -44.91525 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e13d0c3-6e43-3841-9c94-e0ad8c57beef | -8.78232 | -44.71904 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e236db17-ae39-3732-8fd4-95143c62be50 | -8.78172 | -44.71543 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f27e3705-dc07-3819-ad28-cb22b1b245eb | -8.77885 | -44.72336 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8fd1cab7-8402-3eb9-83ce-f8a23837d088 | -8.77572 | -44.92888 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6533be93-a975-3774-8283-dc509517d317 | -8.76893 | -44.71392 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d1eacb92-6854-3775-8729-a8bb2e3826b6 | -8.76833 | -44.7103 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f537ecbb-bbbc-3e2a-a0f0-449ca1e8e222 | -8.76607 | -44.72186 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5f12f42b-f930-389f-bf1e-8f0a6e5c3b05 | -8.76546 | -44.71824 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 931873e7-25d5-348c-b31b-eb508d80f24c | -8.76486 | -44.71462 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 42b90b4e-6b17-3bed-a785-47f43f62ff2b | -8.66604 | -44.87399 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f47a36cf-a863-32bf-be1c-4a7412403000 | -8.66371 | -45.05659 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ce82b7d-fd6a-3bf0-8eb7-1ccdd5b4e0e5 | -8.66311 | -45.05308 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0b8f4d1f-aeaf-3ade-9d42-e534c474ad28 | -8.66252 | -45.04958 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a5b09f15-5e1c-3222-be40-eb9b7e14dcc3 | -8.66032 | -45.0608 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 53fe6422-4fba-3760-a03e-fa080193c87d | -8.65973 | -45.0573 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ab6f367-6aed-3d26-8d4e-d5a79066dafe | -8.65854 | -45.05029 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e7bb1768-4718-3737-b208-fe75a635edfc | -8.65795 | -45.04678 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 019e6bb1-d117-309a-854a-8d92c4bf7014 | -8.65457 | -45.05101 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5f2fd707-1805-3b87-8ff0-8396eda2f59f | -8.62883 | -44.82558 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bb787c33-5aee-3f38-a437-ed93d390e478 | -8.62825 | -44.82217 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 33b5160c-2692-399e-89da-81627178e286 | -8.61212 | -44.82521 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 46675549-a38a-3656-8d60-ff013176bc52 | -8.60256 | -45.12083 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3489b709-67d2-3466-aed6-33aa81fce396 | -8.52211 | -44.27377 | 2024-10-25 16:52:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| a93ba416-5455-3bb4-9ae4-e3a7ef54cc41 | -8.51971 | -44.74883 | 2024-10-25 16:52:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4e2b2a0d-8f81-3e70-8ed4-b80226f0c6ac | -8.51788 | -44.27433 | 2024-10-25 16:52:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| c0add1ad-f430-39b0-91ee-7166125b1b6a | -8.47008 | -44.70377 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa2b8c9c-445a-3918-bbd7-62efdc783354 | -8.43804 | -45.08179 | 2024-10-25 16:52:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ce4f3090-1430-3a11-bd46-8b2b95e0b1fc | -7.99222 | -44.48594 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c98e87df-43a5-397e-b3ab-a3ff143d9a67 | -7.9894 | -44.48739 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00b13b60-0c5f-3236-81c1-02e5f3331fcf | -7.98806 | -44.48674 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5c1d9456-cb01-3aab-a0c7-ca45260e77e3 | -7.98523 | -44.48809 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 087b1808-6853-3b43-b99a-21fbd906175e | -7.98449 | -44.49114 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| faef28a1-44ef-383d-9b89-a2b8f68412e1 | -7.97677 | -44.80213 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38dd1854-59b5-3d2a-b83c-84025005e617 | -7.94204 | -44.8928 | 2024-10-25 16:52:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 67259f42-fce1-3267-a03c-8c7e6ed8697a | -1.55366 | -45.60218 | 2024-10-25 16:52:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f409657-da53-3b1a-9823-e9719c45310c | -1.55193 | -45.60308 | 2024-10-25 16:52:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b34b802-7d58-3d76-a214-1df85e374fc8 | -3.5856 | -45.45981 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| aa92049d-a993-3cb1-b690-a9eaa9d033a9 | -3.58496 | -45.45593 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 230e7872-a264-3e9c-a029-454d8e05d018 | -3.58428 | -45.45598 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 63269c1f-db07-3086-92dc-017d62dab4e2 | -3.58069 | -45.46056 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3136da31-1cae-3082-8bd1-6b17b47dd8ae | -3.48884 | -45.34688 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae22b67f-33a0-3a9d-8003-41ba78d87e92 | -3.48294 | -45.36403 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 296e740b-9ad7-3cda-ac88-3e91558175ff | -3.4626 | -45.39855 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c900d7a-31cd-31c4-9605-65305b642fd8 | -3.45775 | -45.39529 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 207.6 |
| cb575a10-788c-3bc2-b98b-1a714ebc1c5d | -3.70296 | -44.58384 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| ba594a3a-c8c4-35e4-9d91-da4af83e8fd8 | -3.69333 | -44.58082 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7450aea2-98dc-3479-98fa-cd4a5b9763f8 | -3.67179 | -44.80904 | 2024-10-25 16:52:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca1f3a2f-a498-3f7a-bb50-510e170adf3a | -2.65835 | -45.41392 | 2024-10-25 16:52:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9e4dba3e-654b-329d-8368-d7eef767cc28 | -2.58721 | -45.37086 | 2024-10-25 16:52:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e38b62eb-746f-3731-9c32-97d5db57c2aa | -3.6004 | -45.23126 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5bfc557d-4671-3bfa-9f87-d9877ac3296b | -3.59975 | -45.22727 | 2024-10-25 16:52:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 53ee1fa2-08ec-3234-9925-c6197d1433b4 | -3.57432 | -44.8763 | 2024-10-25 16:52:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| e6ae1d5f-b931-3247-9ef6-e005c5d022be | -3.52917 | -45.03817 | 2024-10-25 16:52:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f9d5bf9-81f5-3f04-a2d6-fc39031fd5cd | -3.45396 | -44.82946 | 2024-10-25 16:52:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 14e35a41-1d31-3aa2-9c3e-beea01a719a6 | -3.4516 | -44.70113 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0057c750-6148-3f1e-8832-b7cf1b504c9d | -3.44956 | -44.83016 | 2024-10-25 16:52:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 196cc1c1-be8e-39f3-a277-0a5ddd34310f | -3.43384 | -44.78861 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 102fab74-b476-3ee7-a5e8-8d257faa4713 | -3.42802 | -44.69599 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2f35ee4d-e77e-3a2d-aeb3-90ec3ab1f9df | -3.42182 | -44.99099 | 2024-10-25 16:52:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3bbe1053-0d38-34b2-9c9b-75d87f9da176 | -3.40069 | -44.80724 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| fda84351-56bd-356a-8694-68c57d392b7f | -3.39599 | -44.61074 | 2024-10-25 16:52:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 35f01b88-daf2-39c6-8102-4751183c978b | -3.36078 | -44.69576 | 2024-10-25 16:52:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9db3dbe9-e9a7-393f-ae5d-6b7f6a159b1e | -3.35927 | -44.69361 | 2024-10-25 16:52:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 07c71ecd-688d-36ed-a913-fd4c9782b6de | -3.35634 | -44.69649 | 2024-10-25 16:52:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7298421b-6666-3fd5-8b47-dee1fc57c364 | -3.28034 | -45.12675 | 2024-10-25 16:52:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 169b450f-711c-3204-85e2-f2edef1653a1 | -3.22556 | -44.61235 | 2024-10-25 16:52:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| eaa3e697-98b3-3ed6-9eaf-8f48710bdb46 | -3.22107 | -44.61305 | 2024-10-25 16:52:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d9fcebc7-361c-3300-9480-34658a2000b6 | -2.99577 | -44.87141 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1dc8d41e-2033-3a1f-81b1-396a2372d549 | -2.98855 | -44.85484 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a8b2fdd1-2a1e-3490-b4df-ff2ee5313f85 | -2.95999 | -45.23884 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4706e3dd-c575-399a-a0b9-190981dfdd31 | -2.957 | -45.24776 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 162.9 |
| d71fa266-c9e9-3051-8826-9169fa6e3c2c | -2.95634 | -45.24364 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 915ee632-3c10-320a-91c5-8dfa587fa064 | -2.95568 | -45.23954 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 0e05bcc5-3c82-3737-b1a8-c1d47bc45d52 | -2.95503 | -45.23544 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ff167aca-8214-3f5d-a3c1-df69b3a4ecd2 | -2.9527 | -45.24846 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 01c39e70-af63-369d-9f9c-47afaeb7f511 | -2.95138 | -45.24025 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |


[Clique aqui para ver as próximas entradas](README173.md)
