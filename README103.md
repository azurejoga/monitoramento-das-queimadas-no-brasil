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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 744b7e45-2287-3c75-a0db-ab3bf46f31e1 | -11.11704 | -45.95213 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8837892b-e9fd-3467-aa4d-a9d6473cb2a2 | -11.68336 | -43.65814 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2e26a4e5-e2ff-3d5d-b5a2-e7a5d0014c42 | -9.84295 | -44.78863 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 3c0cb362-99e4-3fd6-aebb-72a026431db8 | -9.86465 | -44.8255 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e24eb7c9-9e5b-3ade-ad03-97608eb0fb56 | -12.87918 | -62.15285 | 2026-10-05 17:13:00 | NPP-375 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce223be7-f38b-39ba-9f1f-bb3813611228 | -10.4591 | -39.50673 | 2026-10-05 17:13:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a5033734-7e3a-3928-8f4b-fe434ca83b86 | -11.83277 | -43.54113 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a82b13a0-0049-399a-a2f1-be67d177e070 | -9.86026 | -44.79473 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 8fcdea03-b04a-3421-b479-1bc772e48ae3 | -11.64113 | -43.61267 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 79a2a6eb-8a3f-384c-b147-41ebb41c9da5 | -11.21911 | -45.38524 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7b250ff-9ccd-343b-aeea-dd89a7cbcd13 | -12.59687 | -47.2192 | 2026-10-05 17:13:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6efcc987-99b0-3948-b352-fcec4998bce0 | -11.81392 | -47.36232 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| afa5bb08-2ae1-3e5a-b4fc-a263d514724e | -12.80612 | -43.31689 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10b2d35b-2736-33ed-96fb-1fa315ddab15 | -11.3431 | -46.65775 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 86d6cb33-25b2-3e64-ad0a-079a22e33780 | -12.54996 | -43.08478 | 2026-10-05 17:13:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a66b1506-e8d2-338d-98ae-0fe03d4b6519 | -12.75372 | -40.03766 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a2509e02-da18-38cd-87fb-46e2257c7a00 | -14.04851 | -42.49246 | 2026-10-05 17:13:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3c4a4796-4203-3880-aacb-ef050e6421dc | -14.98099 | -42.66565 | 2026-10-05 17:13:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f59807f8-c050-39fd-9f1e-ef35d0fda76f | -11.15035 | -41.5643 | 2026-10-05 17:13:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 038aac5f-b6da-3e2f-8dc5-350fcaa5a53b | -9.79256 | -47.78823 | 2026-10-05 17:13:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bc11754d-fb44-3f19-b3f3-d47127cb38b8 | -9.86165 | -44.80839 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b1bf3f88-0750-3cdb-99a7-892c560665d9 | -12.81406 | -43.30816 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| d25c4c3e-d1cb-33e8-aa7d-21e14f8b2372 | -10.1162 | -45.89656 | 2026-10-05 17:13:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f723376c-da8e-33b0-91ef-754cd8e40f27 | -10.95942 | -45.43469 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0cf150b3-48c7-350b-b97c-8dbdf82d5ed4 | -10.66933 | -43.63037 | 2026-10-05 17:13:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0609b1b9-3268-38af-832c-a384eb44a677 | -13.50499 | -61.12267 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b8543632-5949-3530-a67c-3d702dc88512 | -11.34296 | -46.68213 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f760017d-d7eb-3bc8-b692-522fe79e2d31 | -14.44401 | -40.93338 | 2026-10-05 17:13:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ff31cab3-3b69-3b9a-b206-c16bc2cf86f9 | -13.96992 | -40.98452 | 2026-10-05 17:13:00 | NPP-375 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 48cada01-762f-3342-b956-cf9d42ae2374 | -11.65668 | -43.61021 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04d78f58-c739-36aa-9a06-47a9f1fae697 | -10.44629 | -48.31675 | 2026-10-05 17:13:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fef0448a-3d46-334b-89b2-61c57d52d15b | -15.6888 | -41.32808 | 2026-10-05 17:13:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 05bf5377-55f1-3dc8-bf06-a8d1a867a158 | -11.25201 | -43.52002 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3e5ba6eb-d581-36e9-8ccc-a48d775ffa4a | -12.81066 | -43.31277 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 7b9989da-82cd-397c-ab0e-da7c15b8c94d | -11.95985 | -46.39799 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 55a05b29-bf50-3720-b933-a90346844c9d | -11.68572 | -43.67041 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 3829526c-00a4-30ae-aba0-89972cbe5560 | -11.22121 | -47.13353 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e07c0a04-47f4-329d-93d9-4ae57aff0e65 | -12.81459 | -43.30551 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 044c5b00-38ba-3ad6-92e4-06e71e83602f | -15.72894 | -41.80399 | 2026-10-05 17:13:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a7f88f7c-92bd-3bfd-9545-5da131d40e5e | -9.85857 | -44.81318 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8fa742ec-23b4-3107-93e4-d6a5ba13f524 | -12.8644 | -39.92707 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e0b64380-7b0f-39a1-b402-62a65d292d4f | -14.28296 | -43.75592 | 2026-10-05 17:13:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06ba94c3-44d9-3a36-adc6-bc23de7b9823 | -11.34579 | -46.67332 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9366de3a-05dd-3d36-b89c-7bc947192310 | -11.82257 | -47.3645 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4a007375-f86f-3d2e-b779-190845f0fba1 | -11.71714 | -43.49825 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f5b692ac-6045-357b-938f-da53204ce8d1 | -14.86099 | -41.67547 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bd90048f-6af4-3521-8a34-7e0d6682a464 | -13.50187 | -61.13076 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 81591cd0-75ad-3ebb-aaf9-7f07751c223d | -13.51148 | -61.13207 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b5089a3-4982-37e5-a57f-09a8c4888a2a | -9.97172 | -45.60551 | 2026-10-05 17:13:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 403d86ce-8414-3758-b91e-b4e682428007 | -10.23985 | -49.65733 | 2026-10-05 17:13:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7f3406f-c171-3199-b8b4-8bb91163c098 | -9.84683 | -44.78182 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a111134e-eeea-38b3-8b78-0f5a29494b1a | -12.81465 | -43.31131 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| dff53b67-70fa-34bf-8a93-30b0e70b2354 | -14.98216 | -41.56963 | 2026-10-05 17:13:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 37.1 |
| fc40546f-b327-321d-8f07-9b96fb08e197 | -14.1031 | -46.61292 | 2026-10-05 17:13:00 | NPP-375 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4a32a36-a2c4-3aae-b1bb-a0c84d186611 | -9.40665 | -40.3172 | 2026-10-05 17:13:00 | NPP-375 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ba9eba04-a391-37cc-a93d-84b175b186b7 | -13.4504 | -40.05491 | 2026-10-05 17:13:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| 5667716a-2956-3d16-ac12-c9345e5df431 | -11.63141 | -43.61774 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f91cafe8-7bb6-3f8e-8d25-872aad7d72e9 | -11.21077 | -47.14676 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52b01085-20c7-3722-830d-8bff654eb051 | -11.81455 | -47.36588 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0e5da5bd-c076-3959-bc54-dfe7099644f9 | -11.83208 | -43.53743 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 15e1e409-afc5-3d95-a1c7-d084ded6d7f3 | -10.96395 | -45.43337 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d201ccab-5df5-3a3e-ba21-2a70ae4ccb0e | -10.37053 | -48.10292 | 2026-10-05 17:13:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3c2d9a5c-be0a-33c7-84b2-1a1ebb779dad | -14.37126 | -41.89447 | 2026-10-05 17:13:00 | NPP-375 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 8fb1d85f-9b75-3297-a22c-bf62d6ff739f | -14.57323 | -41.39502 | 2026-10-05 17:13:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a7d4f075-31ef-3c95-82a8-8c2a058b2160 | -11.81364 | -47.36359 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da068ceb-3ea3-38a4-8904-2eb3b829d31a | -12.81187 | -43.31902 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2b2385db-7e9d-3974-8a40-cfca17d68555 | -11.1512 | -41.56871 | 2026-10-05 17:13:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ce9bf6f0-b7eb-3245-b742-c28ac5e3ce9f | -12.34872 | -47.06153 | 2026-10-05 17:13:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d2897605-921a-35de-83d9-5e504af9c64c | -11.85467 | -47.3112 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9bda03c-700c-396a-afd1-c047aa146edc | -15.14573 | -42.15897 | 2026-10-05 17:13:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| fa7b0046-a5fe-39df-a225-ca5b6623372f | -15.33257 | -42.77626 | 2026-10-05 17:13:00 | NPP-375 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d8ac118-dd6c-3143-8837-36d1c86d4cdd | -12.33226 | -47.28282 | 2026-10-05 17:13:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f453148a-e9c9-3fb8-a89c-e3e7d2057c3d | -12.027 | -62.54272 | 2026-10-05 17:13:00 | NPP-375 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 827df47e-e09e-3867-9fa3-c04abb66c5b7 | -13.50123 | -61.1367 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d025437d-4738-3b79-a6e2-d2abd0650275 | -12.51163 | -41.68244 | 2026-10-05 17:13:00 | NPP-375 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 42e1abc7-d8a9-3f4a-9f09-77c167d4211f | -11.37839 | -42.55381 | 2026-10-05 17:13:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d553448f-9ede-30f4-bdd0-eb883d2a342c | -11.81425 | -47.36716 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2985fe9c-cdba-33e7-bcea-277b9ee9afd6 | -9.85226 | -44.7788 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 99246a29-2bae-3ea4-8f18-36d07b5b4e67 | -11.12117 | -47.30326 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9c59080-856a-3080-8780-b517633bdb38 | -14.55253 | -41.28571 | 2026-10-05 17:13:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 64cb6411-4da1-348d-a93c-e5063338c85d | -10.95693 | -45.3946 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ca758b77-0d05-3bfe-96f2-7c3b464d8d18 | -11.68134 | -43.65732 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f70c5f48-f57d-3adc-8357-804e6492bcaa | -11.71893 | -43.50778 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f1740ef4-1822-313e-9e35-a3c041827467 | -11.11711 | -47.30407 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58149ff8-cc01-37e5-b88d-247e92c9f2ae | -11.81023 | -47.36786 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 66f523a9-5a8e-3693-8381-7c033654bd12 | -13.51976 | -61.11068 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 26.4 |
| ab011ad9-dd1d-3ad4-b66b-6434597e0144 | -11.68394 | -43.66114 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ca9883c3-6715-3c79-bb1b-f9330a339359 | -10.33532 | -39.48753 | 2026-10-05 17:13:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0c619f5c-5c6c-3b73-a366-831608b7e005 | -11.11258 | -45.95284 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 69007c62-19e6-3aae-b54b-bc874a5f05a2 | -11.6903 | -47.29735 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5420d4f8-5073-3c43-8fae-2cfe33e30ad9 | -11.1615 | -43.49812 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f0e39542-105f-3f1e-beca-12b1cb4390c8 | -14.05001 | -42.49018 | 2026-10-05 17:13:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd0abea5-617c-3016-a4d3-db6ce6d88894 | -12.08458 | -43.41418 | 2026-10-05 17:13:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c0af4549-99fc-3a39-ab96-30b3ca549a1b | -11.35071 | -46.67657 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ca18fd64-5df8-3674-99a3-2878ebf911a5 | -11.64172 | -43.6158 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| e76654c5-7769-31ac-8c5e-862564164bfc | -11.70914 | -43.42699 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2a770534-67c9-334f-9578-cc73d7b164b4 | -10.11991 | -45.89098 | 2026-10-05 17:13:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29c6255f-be20-3928-a859-8327c748e2fa | -11.21295 | -47.13476 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3456e859-861e-3818-839b-061a67e7b40f | -15.19137 | -42.12474 | 2026-10-05 17:13:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 17ead098-79eb-3654-ba48-e592ac17ec06 | -11.44284 | -43.53242 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README104.md)
