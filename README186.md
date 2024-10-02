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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38914b60-682c-3bca-b079-c4ab40d7bfd0 | -16.58377 | -58.23718 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 854b905a-2d19-39ab-b089-81a4aa5ef679 | -16.58372 | -58.23862 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 9f7c0c65-7343-3cf5-96b0-ebf887ab6919 | -16.58312 | -58.24244 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 636757ad-8172-368f-81aa-deddb4bf854e | -16.58311 | -58.2439 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 240e60e0-58c1-35ec-af26-60dc2f05eb0b | -16.58247 | -58.24775 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 186841c2-b9b2-3a5a-88f2-b4f4c71eddd4 | -16.57957 | -58.23264 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 462d7fb7-ead5-3e82-a6f9-46c73fac998b | -16.579 | -58.23652 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| be089dfa-c13e-3a59-ad25-6d7d18546b13 | -16.57895 | -58.23795 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fcf5b01b-4139-3c27-9d5b-c6577d5af1a6 | -16.57835 | -58.24181 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 20600040-cc81-3b13-8556-69004942a654 | -16.57834 | -58.24326 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4f40a1f5-79d5-3b4b-950e-cd42e678de68 | -16.57773 | -58.24859 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| afbf258e-3405-3548-bdaa-d5df0f995a39 | -16.5777 | -58.24712 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6e0c7d08-7d8a-3395-994d-705f926c4b6b | -16.57479 | -58.23198 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ada48d80-c33f-326e-9ccd-acf2951b89bf | -16.57422 | -58.23589 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bcddc134-b3f1-393e-a73f-f863349d3c11 | -16.57418 | -58.23733 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2503307f-f598-3fb1-8a70-6e1f7c263b93 | -16.57357 | -58.2412 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8c85b4ce-a2f4-338a-93d3-4a7f1af7ec6f | -16.57356 | -58.24264 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ff7a083d-be5f-3eb4-8bb5-b067c5c2f7a7 | -16.57295 | -58.24796 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c9cb3cc6-d029-3a97-9142-5c582be9e30a | -16.57293 | -58.2465 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dfdf25ac-450f-37e4-9214-e3c816023031 | -16.5688 | -58.24057 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3ad12746-5caf-3676-9377-d01bd6dbff80 | -16.56815 | -58.24587 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f0858594-6b26-3e78-bed1-e9dc53e70f9b | -16.5675 | -58.25119 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 744e1deb-bfad-3ffe-8626-60683f367503 | -16.19082 | -58.42987 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9d15be2f-ac39-360d-9feb-510ec8add4ca | -16.19019 | -58.43507 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d13d2335-45f2-3b58-bd53-e296abfdecb4 | -16.18613 | -58.42926 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 37eded78-d652-361c-8be5-056f60352d3e | -16.1855 | -58.43447 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3ad970a0-95c5-3d82-875c-2f24f609d663 | -17.03666 | -58.39424 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| da09cd71-aa8d-3ae3-aafc-59e32756ec5c | -12.32647 | -59.2196 | 2024-10-02 05:36:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18f1d6e2-7440-3e93-90c4-dbb6391ef63b | -12.32593 | -59.22356 | 2024-10-02 05:36:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d975bbd-a7db-3958-8a71-5ecede09c7a1 | -12.23261 | -59.24286 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecc9e111-8a92-3153-aa8e-824579004976 | -12.15186 | -59.88626 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 684343d6-bdb1-375d-b7ee-67d2871af822 | -12.15113 | -59.7435 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 288376a0-2e7a-30fd-a181-a4a7d6f24e86 | -12.14785 | -59.88564 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b3d10cf-052a-35d6-a16f-d283d7929c30 | -12.14736 | -59.8892 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f276caa-dc31-3cf8-b64d-7396469d9346 | -12.14334 | -59.8886 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d7dd976-7761-3d82-a324-03514ad152d2 | -12.14285 | -59.89212 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d547a8c-7fbf-327e-838f-d22994ce9f58 | -12.13884 | -59.89151 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9c8afa3-6b5e-3fcc-afd4-58c2a8fa3a14 | -12.13144 | -59.76649 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed3fb4cf-c21c-3eb4-8c3c-8cea5e125b7a | -12.12543 | -59.78028 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3da8c2cd-59cb-3174-b4ec-2aea0327319f | -12.12494 | -59.78382 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05121ef4-e452-313f-8325-c4ab10160f6e | -12.12089 | -59.78327 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 407e1dff-24ce-3aca-bac7-31e94d3b15c9 | -12.12041 | -59.78681 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2d14dfa-7fb8-335d-9e7a-4253f48d792a | -10.98144 | -58.97076 | 2024-10-02 05:36:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44559e26-f367-3dee-a732-9d26d93b2ed4 | -13.14661 | -59.80314 | 2024-10-02 05:36:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4f56a08-7bfa-395a-bc69-1a27527dab4f | -12.34436 | -59.21425 | 2024-10-02 05:36:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a983a6fa-58bf-34e6-ac37-6ba3cc34ffc2 | -12.34382 | -59.21818 | 2024-10-02 05:36:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2ccc8c3-53dc-3694-8c8e-896c21765ad7 | -12.34328 | -59.22211 | 2024-10-02 05:36:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ab7a062-6146-367c-822a-938e2a73ec59 | -12.34015 | -59.21366 | 2024-10-02 05:36:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec8c3589-8648-3d9d-9242-9cfbd418363f | -11.33904 | -60.56091 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f11ca53-ee52-33ea-ac83-f5977a791f39 | -11.33784 | -60.56221 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 322dd010-f6c1-3f78-8dcf-466d50459cd0 | -11.33138 | -60.55997 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf3fac7f-2d7e-38e9-89ce-9d420b2edb7e | -11.33018 | -60.5613 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d6e6321-ec78-328a-9a42-206c1dc72a47 | -11.32757 | -60.55944 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9202b8ad-0d08-3ae0-865f-e6de217271e4 | -11.31928 | -60.5629 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f1ebb13-b8a1-32a5-9977-4b09f107f565 | -11.31859 | -60.56765 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a59cae3-dba9-3dee-bbde-1496f9a65726 | -11.3058 | -60.5754 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81ca5aca-8ab2-3b79-bc77-98fa1dcc037a | -11.27553 | -60.62389 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c63115b-9042-31a7-809b-81592c649260 | -11.27506 | -60.6001 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52356252-4f51-3782-9281-4af1ae5cf025 | -11.27237 | -60.61893 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e0e768c-bffd-30b0-992e-4eb045ec8de6 | -11.27191 | -60.59499 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b1ab7a-1091-3707-b255-cc3bfb4ae291 | -11.2699 | -60.6091 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f1ffbc2-0de2-3fcd-b894-7e73c8724280 | -11.26363 | -60.59866 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c7a016e-f260-3853-acec-8ca3ae757a4a | -11.25983 | -60.59811 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 385c37b2-fd8a-31b1-a038-aa6e6510d0a5 | -11.25603 | -60.59755 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a841b9e-6467-3bc6-b8ed-7b3de2b82bea | -11.25224 | -60.59689 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8775b5cf-cc6f-3e1f-aa23-554d1bcf601f | -11.25161 | -60.60133 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f84d2d2e-4bde-3887-aed8-ee797bec6feb | -11.24847 | -60.59614 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ba8acffe-dcb8-3df7-9f9b-76c5347cc9e3 | -11.24784 | -60.60059 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d22b55c8-d7fb-37ef-8f5d-85bef85e89f3 | -11.2472 | -60.60507 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 033831ff-470a-3628-9649-d53b18f44d99 | -11.2454 | -60.47945 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fd86bbe-0221-3bb9-b469-e4cda07d6c44 | -11.24406 | -60.59989 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d9e4fe22-03e8-3e1b-b0c6-0fdcaa6ee6e7 | -11.24312 | -60.47636 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bb7bee6-bb36-370f-92e4-272e599c3e87 | -11.24227 | -60.47392 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42b0863d-1513-382f-883b-702239038cd1 | -11.24002 | -60.47089 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c79c86a-411a-33be-9821-0470056f06fa | -11.23913 | -60.46843 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2123a190-c4e3-323c-91ea-a8772fcfcd97 | -11.23691 | -60.4654 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d7da03d-21c8-31a2-b014-c2f98e77e147 | -11.2362 | -60.47023 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b38c0ff1-f344-3089-8344-0d4ecdb7886a | -11.23531 | -60.46777 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ada1f55-f779-34ff-9f4b-31211cc321a6 | -11.23149 | -60.46709 | 2024-10-02 05:36:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 240fbc13-2c6e-3f80-b65c-b8c5e7bc65bf | -11.19881 | -61.28401 | 2024-10-02 05:36:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0f2c204-c1e1-3512-9cd8-2b9eb8c44c06 | -11.17527 | -60.64916 | 2024-10-02 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b132459d-aa45-3174-a2f7-487dc145376f | -12.30971 | -60.75934 | 2024-10-02 05:36:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb87a035-8dbc-32ac-bb84-0dfd768b0e75 | -12.3059 | -60.75879 | 2024-10-02 05:36:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3600d5e5-bc78-3b23-a5f4-879bfb364508 | -12.13897 | -60.76868 | 2024-10-02 05:36:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8054c6e-65a0-357a-8ba5-0deba5cdb6de | -12.00034 | -61.08558 | 2024-10-02 05:36:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a0583f0-364c-303d-9be2-51d5eddc8005 | -13.28912 | -60.81702 | 2024-10-02 05:36:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3bdbc97-055d-3dd3-bcf7-d5251bd441ee | -10.65241 | -61.75464 | 2024-10-02 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0aebdebb-b444-3804-b600-069806b79152 | -10.63758 | -62.81611 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8b528c9-00af-31e7-b5eb-057757ffb571 | -10.63702 | -62.81981 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e9bb5bf-115d-312b-a1bc-6fd11c8bd52f | -10.92792 | -62.44753 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ca63673-3092-37a6-bd75-860eb9990ed0 | -10.92736 | -62.45121 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b4cff35-ffe6-3319-9fb3-9eee13f343b1 | -10.92391 | -62.4507 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ec1c04e-1fff-37b0-a3f5-6394c742f70a | -11.31353 | -62.07077 | 2024-10-02 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77ac471b-3156-32dd-b44e-1a38b21715a5 | -11.31001 | -62.07022 | 2024-10-02 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd65aea0-7ca3-3433-a90a-182e01a9b18c | -11.91697 | -62.63488 | 2024-10-02 05:36:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 870938d0-dc36-3758-bb13-4d90affe9445 | -12.26733 | -62.31555 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a2026f3-0763-3531-890d-d1a2358963f4 | -12.26668 | -62.31619 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e5c54c3-8836-3e61-9bba-b896335bf01e | -10.90547 | -62.61911 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2480053a-457e-3ca4-b4d0-4c42605ae9af | -12.88229 | -62.77538 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38f1f4bc-c80c-3497-b488-b9945e8f0b1d | -12.87825 | -62.77874 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README187.md)
