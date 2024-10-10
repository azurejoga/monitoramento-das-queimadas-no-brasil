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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3216bcce-0791-3269-8e16-a1a46d505c42 | -9.91084 | -58.68282 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d70028f-036b-32c2-b360-3c098f94d537 | -9.91014 | -58.68835 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38f9014d-7abd-3c37-bcdb-17d0a8615384 | -9.55865 | -58.96384 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff4ffafd-910b-3124-ad99-285a4f863533 | -9.55293 | -58.95862 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a47d64c4-7096-373d-a8fb-fa8ed8f71b24 | -9.54893 | -58.96115 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f3f590a-f478-3bb7-8c5b-e07cecbe31aa | -9.54663 | -58.95776 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6485ad4-20f4-3313-b681-549dcf070efe | -9.54603 | -58.96244 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12cd2867-eb0d-3f64-b475-5daa02356374 | -9.54265 | -58.96011 | 2024-10-10 05:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 375aba13-2980-3548-a742-d72d86e0e1a6 | -9.46709 | -59.03125 | 2024-10-10 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25d3eb88-5635-376f-99ac-06557af2e9a4 | -9.44545 | -58.94796 | 2024-10-10 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fedf5a0-63fb-3a0f-985d-88628d6c0794 | -4.52823 | -59.90039 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc6a148c-6c2f-3770-9976-2c716c850696 | -4.52435 | -59.89705 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43877db8-4af7-32e9-9619-7e4dd113c424 | -4.52381 | -59.90067 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20845e2b-665c-3bbc-b575-bc1eb543bfdd | -4.52269 | -59.89962 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 005a7289-7268-3b4a-a50f-cc5ee9c160a1 | -4.37743 | -59.93907 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc8b9f34-3183-3ce4-afa2-f71ce885ab0b | -4.37692 | -59.94258 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f450ea3e-3bfb-38b2-98a1-c7e25dfe88cf | -4.29387 | -60.01364 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de5d9154-caca-3116-bb9d-8a415d24b1dd | -4.29369 | -60.01473 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d66323bd-22e0-316c-b41c-15080aeb7d0a | -4.29337 | -60.01717 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2f8a2c8-1b8a-343e-ad1b-50d7f366cf71 | -4.29316 | -60.01824 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2e27f2e-91c8-3f09-8dae-759de42fa4d2 | -4.28874 | -60.01037 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbc7ec3d-d057-32ea-9d34-fc4219806d2f | -4.28822 | -60.01389 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dc8ff81-33ff-32b6-9cbd-762f5af85466 | -4.26796 | -59.88401 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37d7e3e6-01c6-34ab-accb-d63903a55d55 | -4.26745 | -59.88759 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 124807f9-292e-3cb8-8401-b4300cfbe55e | -4.26693 | -59.89116 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a88060b-622e-3d7a-b2f5-d2485086758d | -4.2609 | -59.89391 | 2024-10-10 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07b2348f-a7cb-3f67-bda6-8ccb5b20251b | -4.25743 | -59.99506 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e13835ca-5424-3b6a-8887-5e6bc301bfe1 | -4.25691 | -59.99859 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e2dd8c0-918c-3e84-8e1b-909e0926c2c1 | -4.25247 | -59.99068 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96d67018-cdc4-3148-bcfe-a8b4fbd5d271 | -4.25195 | -59.99425 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2260e5a7-7423-34bb-a586-f413d0fe5f2a | -4.25144 | -59.99777 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 158dc588-49fc-388a-8a92-bf9c452b7fee | -4.21363 | -59.98852 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9da6f1f2-e5d1-3533-b8ba-e36fb29ff041 | -4.21312 | -59.99207 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e081e2-3670-3da3-b2ba-e4176429d6ec | -4.21235 | -59.99118 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51c04f0f-fee0-328b-8f24-b126f649684b | -4.20816 | -59.98767 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3787dfdc-e33a-3a66-a5e4-54d7dbc0eb83 | -4.20765 | -59.99123 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7728c042-e202-3653-84a6-762bc5c9970d | -4.20714 | -59.9948 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8580076d-2fbd-31b9-81e7-ef21211c9daf | -4.20688 | -59.99036 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20cc5f08-78d6-3457-ab98-e49a278ee1b2 | -4.20635 | -59.99393 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 988e9995-3271-30fa-93aa-890ef2861359 | -4.15832 | -59.94004 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a08a59ed-e1f1-3a26-b660-7f7da21620cd | -4.1578 | -59.94359 | 2024-10-10 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31716bbf-9d99-3f57-b64d-77137f2e2191 | -5.29705 | -60.09733 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d9f39f8-2aa4-3d7a-a833-3ca476c1b383 | -5.29654 | -60.10092 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91410990-8c65-3b4a-9029-336f8ee5787e | -5.29603 | -60.10452 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ce8aa86-80f1-3295-92df-77fd5c68cbb5 | -5.18131 | -60.27648 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e3d20be-303a-37c1-926f-291dc9672957 | -5.1808 | -60.28 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 897ddad3-2d97-3fa1-9442-95bcaa0f82bb | -5.0882 | -60.22323 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd9648ac-c6e4-3e73-88f5-67c0957b3ef2 | -7.14804 | -59.3067 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee52db7a-2cde-3e69-b8fc-0dc1b32b6115 | -7.14207 | -59.30584 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0539a63-992e-3be4-a63e-5ec17b689a33 | -7.13789 | -59.38074 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dda316ae-525d-383a-b0ec-442b3a5c57f5 | -7.1361 | -59.305 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6da53b0b-09b7-3448-9b1f-956c8580204b | -7.13255 | -59.37551 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 652fc383-dade-3ec4-b92e-dfac8fe753a5 | -7.13195 | -59.37989 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 532c3cc9-3b24-3c99-91b5-6443c358ebbd | -7.08705 | -59.26223 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 392943f4-6fe4-3805-9cde-1a19952fd862 | -7.08464 | -59.26018 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fdf2a51-b729-3b09-9a21-ca9c2181d729 | -7.08403 | -59.26459 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24fa6d61-aec1-3e72-9ff3-a7709185f4ba | -7.08106 | -59.26147 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 724f1a10-bf9b-3357-ac5e-56c077fabbba | -7.08048 | -59.2659 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b91a3f38-3b73-3845-a5bd-5088a1b6d552 | -7.07803 | -59.26386 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc38ab74-fa54-30b2-875d-08e123a8f97d | -7.07742 | -59.26826 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc7abfec-5c48-3708-b0b7-e8da13a33e6e | -7.07448 | -59.26513 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be12f370-9e22-3c3a-b9f7-089ebaff9439 | -7.0739 | -59.26955 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2ef0c23-3194-35ad-a8fb-6d63fdc19d64 | -7.07143 | -59.26752 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82414aa-9d00-36d3-90ad-b6572dda7771 | -7.03975 | -59.36483 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d92e617a-59b8-3dc0-82d6-45dcce56df4a | -7.03697 | -59.36612 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52db4ed4-8516-3e40-ba26-935704a078db | -7.03643 | -59.37033 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41de5f00-b992-35fc-934f-292ebc4572d3 | -7.03381 | -59.36399 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea5c0a65-e836-3f29-9526-313fb580eb35 | -7.03323 | -59.36821 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7cf7a9d-3f89-38fc-a5e3-a76de50ede4a | -7.03264 | -59.37248 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd0e582c-9b91-314e-8041-1a2554e2d03d | -7.02729 | -59.36742 | 2024-10-10 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fafd023c-2750-38fe-8b02-7d2f65204e95 | -6.78191 | -60.04473 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb8f34e9-cdd2-3310-bcf7-58f65a1466e5 | -6.7814 | -60.04848 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9e218d9-0e61-335e-9eb0-1f74d79c18e6 | -6.7809 | -60.05218 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b4afc47-671c-3689-a138-3618090ea21f | -6.77623 | -60.04407 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4745867-a28b-3395-a732-70618d852cb5 | -6.77572 | -60.04786 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541a7989-ee80-3edc-b401-63d48b4304fb | -6.77521 | -60.05157 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3aa5477-f5d1-3b2c-b4a5-e661393c606a | -6.77471 | -60.05529 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3626a9aa-3abe-3471-9743-6f28564ab634 | -6.77005 | -60.0471 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a1c7c60-cf8b-3375-882e-eed19c8ac9b8 | -6.76955 | -60.05084 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2ad55cf-41df-3352-ab64-5dcbba891347 | -6.76904 | -60.05455 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddd1480f-3d8c-380e-a7c8-fc891ebe8999 | -6.76855 | -60.05821 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5242915-d79c-384a-80f9-4f38cfe86c16 | -6.7639 | -60.04992 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4eac13c2-92e1-3818-983e-566fa86dc419 | -6.7634 | -60.05366 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f505af0-22ea-3625-91fb-608a32dcfec6 | -6.76291 | -60.0573 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d12eb55e-191d-3645-95b3-20361f8702c0 | -6.71794 | -60.11073 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78d9c7b4-7640-3058-af89-49e8c1701f98 | -6.71743 | -60.11433 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b12ac50d-2016-364e-a706-aa33e489c3b8 | -6.71231 | -60.10992 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bc390f0-fd38-306d-9b0b-de069f400fe6 | -6.60441 | -59.99958 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ec7bbfe-3509-3c72-b65c-f6ce562da3f3 | -6.60389 | -60.00329 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1d307d0-166b-3012-b9bd-64bbadbbb7dc | -6.54982 | -60.0191 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6528224b-419b-33ee-9d7d-d5a9a4faea00 | -6.54808 | -60.0103 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f2d8340-bb51-3333-bc99-ec27f29b1156 | -6.54754 | -60.01409 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bfcc1b6-b429-3974-961d-0895a4a0f1ff | -6.54699 | -60.01796 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 931cd395-ef76-33be-8096-e0335cd0e8cb | -6.54673 | -59.99928 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ffab5aa-03e4-3736-9160-fcc8781a46ae | -6.54621 | -60.00311 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ac56c43-1151-3f2c-9b93-fbbd5ea437be | -6.5457 | -60.00688 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de0deecf-035e-3e44-a855-ae9138d63f6f | -6.5452 | -60.01061 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33de252-824c-3d64-b813-2b6a165b43ff | -6.54469 | -60.01443 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47503df9-2acb-3e7b-960b-91053b55bdfa | -6.54417 | -60.01828 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9634727-2582-3ef4-b615-73d56a927084 | -6.54404 | -59.99811 | 2024-10-10 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README142.md)
