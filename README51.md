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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f991ea18-6e3f-332d-b2a1-664e73c90b68 | -9.16216 | -59.37078 | 2024-10-03 02:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5b34f6ce-ef72-3be6-8dda-0030449eb6f1 | -9.16098 | -59.36514 | 2024-10-03 02:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4c1d60e0-d12c-3aa0-8e6c-c660a6e57adc | -9.46867 | -58.97932 | 2024-10-03 02:09:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ec7d380c-a988-3678-9a58-3a50f22739f2 | -9.46537 | -58.97429 | 2024-10-03 02:09:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4da371d3-a148-3beb-adee-6ee81c7f4090 | -10.70036 | -58.56851 | 2024-10-03 02:09:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 7b014c03-dfc2-34fe-8956-deb1d844d086 | -10.69679 | -58.54698 | 2024-10-03 02:09:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0aba60cc-ab24-35ab-8aa5-64f8d2ed757e | -9.93312 | -59.92304 | 2024-10-03 02:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 373a6103-357e-32dd-a349-64769b165b36 | -9.90987 | -60.08582 | 2024-10-03 02:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c20e8cf5-50c4-3e30-b4d1-fececc4132a5 | -9.90438 | -60.09328 | 2024-10-03 02:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1a1f174d-619a-312c-9a0b-62543023c24d | -9.90177 | -60.07637 | 2024-10-03 02:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8c5c51f5-6fc1-39de-8d54-0c0615baa5ac | -9.39632 | -61.05986 | 2024-10-03 02:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 3680e248-e784-363b-9661-a20d75603652 | -9.39408 | -61.0451 | 2024-10-03 02:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8ad35203-2d31-3cb0-982a-b700a10c3112 | -9.38518 | -61.06168 | 2024-10-03 02:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 100bce91-e8a0-3e38-85be-21bdbbd6aaa6 | -9.38292 | -61.04688 | 2024-10-03 02:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 787d9792-e84d-3e69-b95b-2f3f75170c93 | -10.37727 | -61.21367 | 2024-10-03 02:09:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d32ecbdb-5f6f-3e98-850b-1948102c9156 | -7.90488 | -61.47509 | 2024-10-03 02:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 68a2f0c4-f628-3b18-8aac-a68325dcbaac | -9.17062 | -61.68606 | 2024-10-03 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 68a14830-9bc2-3ff5-8a4b-2e5983e38a5b | -9.16857 | -61.67271 | 2024-10-03 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 100.4 |
| d1d5259b-63e6-30f8-8b76-f02b182be12d | -9.16651 | -61.65928 | 2024-10-03 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8e165fe6-5a53-367c-99cd-3189e6e8c157 | -9.15791 | -61.67447 | 2024-10-03 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 52a330e5-3ccc-348b-b3f0-fcf4489bf763 | -8.89065 | -62.3387 | 2024-10-03 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 37f2d455-9ed4-3834-a81d-fc370ca4b966 | -8.88043 | -62.34028 | 2024-10-03 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0af642b5-4865-3315-b591-7d6c1d18c2a8 | -8.87064 | -61.8524 | 2024-10-03 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 35359ece-0ca9-3932-9286-2f30a24c21a9 | -8.56516 | -62.48749 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e08794c2-4be6-356a-9731-57dbee86459a | -8.17902 | -61.37799 | 2024-10-03 02:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b3627606-6bdf-3c56-8a4d-1f0b0894a142 | -8.17877 | -61.38374 | 2024-10-03 02:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dea30fcf-7e29-3daf-9600-00c98546c2a7 | -8.17661 | -61.36916 | 2024-10-03 02:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3f5f3e51-5339-3993-a3f0-de3cf7fa37dc | -8.8888 | -62.32655 | 2024-10-03 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 22febf75-1e9e-3241-80fc-dbc221be9a9c | -8.555 | -62.48906 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c846ade2-30e6-3015-866d-2a0f2aac372c | -9.43979 | -62.10352 | 2024-10-03 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 946dc8ad-f170-3ed5-9784-86ef516514ca | -10.03634 | -62.46113 | 2024-10-03 02:09:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 883a6bf5-b6e8-313e-a3ec-9812476d78a1 | -10.64314 | -62.81919 | 2024-10-03 02:09:00 | TERRA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cff67680-30ee-3519-9ad1-6dd4737715fa | -11.34162 | -63.04513 | 2024-10-03 02:09:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 03bfc1ba-458a-30cf-9b39-fe127761a157 | -11.31064 | -62.07874 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d6f5db2a-d19b-3252-8b37-ea5b18d77010 | -2.88225 | -61.87421 | 2024-10-03 02:09:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 16020538-ab40-3037-96a6-168e6dc16c5a | -7.58871 | -63.36243 | 2024-10-03 02:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d56eb6b7-2ce2-37e3-ba4a-d1f7002549ae | -7.03536 | -63.08308 | 2024-10-03 02:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e16c77e3-2d10-3e17-a3d4-06f002147a27 | -6.85683 | -62.91346 | 2024-10-03 02:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d4a60a3e-c58e-3378-80f3-f1d1c511a1ac | -8.96482 | -63.61701 | 2024-10-03 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c2573cd2-758e-3902-9dfe-3785584fe3f0 | -8.96335 | -63.60681 | 2024-10-03 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f5ace7d2-77a5-3619-a490-d6ab35a6f19e | -8.38725 | -63.35142 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60a7dd06-5674-3d44-a9b3-17e11a329758 | -8.62213 | -63.29256 | 2024-10-03 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16a24853-eb7b-3e3d-be3e-88e62d28b65f | -8.59855 | -63.13054 | 2024-10-03 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 16d6f064-8b3b-31d0-9e88-9015853371c8 | -8.45883 | -62.66704 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 0d506e2a-c2b8-3091-a5b5-9dd1f9ed4b1d | -8.45825 | -62.66143 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 039bbe82-90fd-31f5-ab2f-36e4f57b9813 | -8.39845 | -63.36058 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ebd0ff4b-90ac-3d84-8851-91788d2496e2 | -8.38883 | -63.36207 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 29ee936f-b153-35ad-b076-375f9bc209fe | -9.19762 | -63.44764 | 2024-10-03 02:09:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| dbe66964-a33b-3e4c-8ece-cf6b405bd74e | -8.95393 | -63.60824 | 2024-10-03 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 54129d43-2040-3ca8-b99e-13d2696358fc | -8.46711 | -62.6538 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 77444933-6158-38f6-a9ac-10956b13bd7c | -8.45995 | -62.67315 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1184cc5e-25f6-343d-8103-837426543f30 | -8.45706 | -62.65535 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6dc8b68c-e5d0-3201-b06d-21d18e4debc7 | -9.96278 | -63.00649 | 2024-10-03 02:09:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a3fe5347-78f0-3b0d-bd89-5d9721eaed9c | -9.96122 | -62.99584 | 2024-10-03 02:09:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 03218449-d217-3a8a-a0b1-d20f8432d318 | -9.78358 | -63.93567 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 91643206-b88d-3a64-ba9c-dff60f3c1589 | -9.77438 | -63.93703 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 47c4f44c-8064-3334-b932-94f52892e926 | -9.76077 | -64.28737 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fd0fd284-8177-3a24-b704-00d176758b6a | -9.75305 | -64.29815 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 42568b5b-6237-309d-a3c3-1b3c58248b6f | -9.72673 | -64.24432 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e85a86f6-48e3-3af3-b902-2d44445b60d6 | -9.71763 | -64.24563 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09f50e5a-d60f-39d4-86af-06f8321959b9 | -9.71627 | -64.23623 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1704d91a-b78d-30cd-ac0c-86e12fd62e34 | -9.54633 | -63.14968 | 2024-10-03 02:09:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 25.4 |
| d0c3d246-9282-33ac-a6ce-e1c64bb99ce4 | -9.5435 | -63.15591 | 2024-10-03 02:09:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f7aae7a1-6cf6-3ffb-825b-0da224b7f047 | -9.51224 | -62.92331 | 2024-10-03 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 47d1a173-18d7-3405-8f4d-bf90005e8a6c | -9.51066 | -62.92937 | 2024-10-03 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a67d294b-843e-33b6-af34-b1927dadc6fc | -10.615 | -64.52265 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a1321361-f8bf-3b07-9797-c672ea31e232 | -10.61368 | -64.51344 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 266c7bce-e3f3-3b68-bd00-8d0a1964199c | -10.56643 | -64.50806 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d57f207-fdbb-3856-8c54-71bd25c01ba7 | -10.56514 | -64.49892 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4d06fb22-7f16-3cde-acd0-d42c289b80e6 | -10.55485 | -64.49095 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cd35f26b-1a59-3673-a3e0-785b23ce0327 | -10.55355 | -64.48176 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ab4eaa5-a9da-34ff-b5ad-a0acdf89e88e | -10.1118 | -64.4207 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dac7b9c3-47c7-3482-9491-8a27c1697b54 | -9.7758 | -63.94675 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d9cf31a9-90af-30fb-b273-a38e1533e325 | -9.76212 | -64.29679 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 775fc30f-7938-3134-9559-d123795f9405 | -9.7517 | -64.28873 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a0eefb11-b7db-3c9f-8e36-33b5921d99b3 | -9.73652 | -63.98877 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 745dc0bc-91f5-364d-b9c4-9c79243bcb47 | -9.73513 | -63.97906 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.9 |
| fb10633a-4af2-3113-9bfd-868250bdf4fb | -9.72536 | -64.23486 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 30beb341-31da-3e30-88e2-df90f99065df | -9.7149 | -64.22684 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f816439a-d349-325f-a274-c5efe58a56f5 | -9.54195 | -63.14522 | 2024-10-03 02:09:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 41954b50-4a56-3caa-943a-f379ec52683a | -9.52338 | -63.61363 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3a0aa7c2-b985-3f23-802c-e55d15d18266 | -10.7016 | -64.16202 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c8953b3-59b1-33f0-aca1-ed8b25bd47eb | -10.70026 | -64.15265 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ecdb39bf-415e-39f8-8edc-3f599fb329dd | -10.69892 | -64.14319 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3bc4d571-4864-35f5-a07f-817537085484 | -10.6912 | -64.1539 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5d6cf985-175b-3733-afda-efdc58b68522 | -10.63291 | -64.51993 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 17216362-4194-342b-aa7c-836d1f8c6d5a | -10.62396 | -64.52136 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c930a6a4-fa9a-3696-b13f-7b8269f1fb0c | -10.62265 | -64.51214 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd9b63e1-35ca-37ad-a7fb-c50c9b043f46 | -10.62183 | -64.05828 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| afdabad5-2528-3772-bec6-39ed1dd90673 | -10.61275 | -64.05966 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 305fe912-2955-3548-a4f7-be492034fd5a | -10.61135 | -64.05007 | 2024-10-03 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 797c8833-2a0c-39cb-833c-4c03970e13bd | -10.57885 | -64.01215 | 2024-10-03 02:09:00 | TERRA_M-M | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fd13cdcc-27fc-3e44-b96c-7f6f9b3f3554 | -10.5775 | -64.00272 | 2024-10-03 02:09:00 | TERRA_M-M | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cffe9d67-2eb8-3503-ba61-c46728f75faf | -10.36784 | -64.08549 | 2024-10-03 02:09:00 | TERRA_M-M | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 491f40c5-5865-3b40-af2d-1671a9593355 | -11.6215 | -63.82906 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 74bf5818-527f-3e42-8292-93d5ecfbb4de | -11.61516 | -63.84933 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7237e819-65a6-34a3-bd0f-6d12779d1c18 | -11.60627 | -63.72413 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 60632d47-88a8-3753-a60f-cdd8a159b8d9 | -11.60486 | -63.71443 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6ef31fc8-0578-3285-a2e9-b2bd3f1c7936 | -11.58448 | -63.7665 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c18f519b-2f34-3831-872b-fd2c37cf3d25 | -11.55887 | -63.77636 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README52.md)
