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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2314e42-4268-3af6-9294-3f204098743b | -8.81308 | -58.20078 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6594b84-df55-3555-a51a-2b9483a2edf0 | -8.80952 | -58.20025 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d98c85a8-2704-3f08-8aaa-6336a4854863 | -8.80891 | -58.20429 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a3ebcc6-44ca-39ee-a21d-cc76278e65db | -8.28816 | -58.15117 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75322394-d18d-3b03-b906-2303efc8aa14 | -8.28461 | -58.15066 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ff19e21-768d-3639-b38a-60f2ca141cf6 | -8.26804 | -58.77854 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5ecbce6-fc37-3f4f-86ec-5da3a77f5de6 | -8.26688 | -58.78611 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef23d6a8-36df-3244-9377-40d483acdda6 | -8.11215 | -58.04713 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 745dfcdd-f190-37f5-a235-cda226edb686 | -8.1086 | -58.04658 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1cd50ff-c709-3115-889b-9c97ca026d06 | -8.10505 | -58.04602 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6c5038c-2fcb-3248-b508-7b649f477ca4 | -9.34877 | -58.96442 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d541ae1a-9899-3762-9436-d93656fa98f1 | -9.3482 | -58.96821 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d99cd8bd-c5e8-332c-9ca5-6e6213c04454 | -9.34523 | -59.03376 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c55b131f-9c89-3691-8665-609f67ee4a23 | -9.31743 | -59.28201 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28ff9d00-a5cb-34e7-8b61-8f0e1b25957e | -9.3141 | -59.28213 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0013ddc5-3123-34b8-94d4-988776651431 | -9.31068 | -59.2816 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f152cce-c232-3a08-b778-1fa2d4353115 | -9.30726 | -59.28108 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f023604c-0102-36c7-ae30-e590f8c51a60 | -9.30669 | -59.28479 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de94104b-4544-3991-b29b-9c14ffa6e4db | -9.26744 | -59.40369 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 0f386ad3-3274-370b-8e37-a92f8b4e7ad7 | -9.2646 | -59.39946 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44b61523-099f-3c93-a689-462ff13f5383 | -9.2612 | -59.39894 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3306ee3c-3682-37ad-9754-3ea986db5825 | -9.23968 | -58.9486 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff95ef5-4fd4-3242-a485-5d883a862c09 | -9.19299 | -59.59461 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcece751-d013-3a63-96bd-51e7a95f38c8 | -9.17091 | -59.37438 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c00efe6-c87e-336e-b33d-94e7b26e4b29 | -9.16978 | -59.38176 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e45a674-a521-3e72-8f4a-587a5111f155 | -9.16807 | -59.37015 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e84f052-c886-3979-b209-2ecda1baf6ca | -9.1675 | -59.37385 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df7d81fa-53bf-30ae-8796-8856774c6fba | -9.12096 | -59.01658 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97119c7d-1dfd-3652-adfd-e6a4047c2a80 | -9.91155 | -58.28646 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb872e07-2ca9-3f04-b5d8-dc435306bd93 | -9.89213 | -58.68658 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 314aa410-6b47-36a8-a62d-e95bb94683ff | -9.69579 | -58.65103 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 261eeb21-cecd-3918-b430-51b42dd30e1e | -9.69227 | -58.65049 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc327c9b-2775-3c84-9c5c-8641a09209f2 | -9.69168 | -58.65443 | 2024-10-12 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f3f53f6-fe20-318e-a657-48ba0a0d0c5a | -9.78734 | -59.01691 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28f4a042-1949-36fe-816e-2d006cd8578d | -9.78587 | -59.01583 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ca6eef6-e9f3-3547-97df-291509e80e7f | -9.7853 | -59.01965 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0112cb2a-a410-3e72-afa1-f7bb30750a32 | -9.78388 | -59.01637 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ed23354-d900-385e-8869-43abeb047194 | -9.7833 | -59.02018 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 116431c3-b9fd-3af8-a3e1-1d3c6a754d7d | -9.78041 | -59.01585 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e094f30-7ec3-373e-86f9-e886f7c94d32 | -9.77983 | -59.01965 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29d52a02-7a5e-3874-a43b-a1ef28953b4d | -9.75721 | -59.30179 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e205698-86e3-3238-b4f8-e9653d66b6ca | -9.74446 | -59.27364 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24cd981a-81d1-3e1f-9a96-d4f6bb87fad8 | -9.55035 | -59.03698 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a2bcb58-b71e-3259-9a98-90674c54e495 | -9.54091 | -59.41829 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2c1a6c6-cc8a-3e54-ac85-cf739229d953 | -9.52212 | -59.10629 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52aa562a-6ca4-3ec7-b52b-c5714857927e | -9.39331 | -59.3355 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ea22e98-ea19-39a3-9860-623388822826 | -9.38591 | -59.33814 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7316bcf5-83ba-36b2-a8bd-f1d65a255cc1 | -9.36442 | -59.52351 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e46a8e0-22c4-3d09-88f8-e6ca04085d35 | -12.3373 | -59.87297 | 2024-10-12 05:23:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4576f6a8-f1e6-355f-9143-ae16895448bf | -13.15111 | -60.4122 | 2024-10-12 05:23:00 | NPP-375D | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41f571e2-bc01-3242-9085-9eec28f03759 | -13.15056 | -60.4159 | 2024-10-12 05:23:00 | NPP-375D | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee969a10-4e2c-3691-8bff-f2350a21a10f | -12.9654 | -60.0522 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee8b6ad3-a14b-3542-97b2-033005b730ac | -12.96482 | -60.056 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd756ce1-8197-3121-8d38-9f0e5bfd38f5 | -12.96139 | -60.05548 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75acff78-6e4e-3754-9da6-1653147a2cf4 | -12.96082 | -60.05928 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdd4e22f-3554-3d83-a560-0d974d3e7fe5 | -12.96024 | -60.06308 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0351fb93-9b37-3b62-a789-02e1f8691292 | -12.95681 | -60.06255 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8365de6f-acd6-3264-be95-6dfeffc66077 | -12.67893 | -59.82607 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 787fdcca-3a67-39a5-8c07-5d5a505a8853 | -12.67835 | -59.82989 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c24abc26-2bdc-399c-a81c-454b84d7598a | -12.67777 | -59.83373 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98c192e2-db6d-3544-b578-c09a4ad4651f | -12.67663 | -59.81789 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e22e0fc-6ee1-3231-8225-f38aa5e29da1 | -12.67605 | -59.82173 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0d93e5f-a54a-3583-bcc6-f46b69aef5f4 | -12.67432 | -59.83321 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e48da435-cf29-31e5-814f-33380829b00d | -12.67318 | -59.81736 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd4df536-7d7a-37e3-a26d-a4f9d3f3688b | -12.66973 | -59.81684 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7228a981-70bc-3d5a-a432-bbe2d3153d26 | -12.66683 | -59.83607 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acf064ff-0a5d-32aa-b2f4-2ab99eaac42d | -12.66337 | -59.83561 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14d86da9-a46c-3b82-950a-c5ab5b71c123 | -12.6605 | -59.8313 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35df2af9-86b7-3332-8b22-8fed2d84d0d1 | -12.65762 | -59.82698 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efaee7c4-4ba5-3a4a-a228-3c968dd56d31 | -12.65129 | -59.82214 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35d839da-9063-33df-9c90-1ebf167a61d6 | -12.64493 | -59.67549 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0f2898a-da55-3578-9633-0c0eeb1f827d | -12.64441 | -59.82104 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc43d6f7-4c25-32af-863c-06291d51a43e | -12.64377 | -59.65939 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9efb0c22-b5f7-3424-a606-161255189beb | -12.64096 | -59.82048 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 574108d8-9cd3-3d6c-bba7-0759130cb3fc | -12.63408 | -59.81936 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44d8efda-57e8-3076-b4b8-41c8936d271f | -13.74523 | -60.12095 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| deb801ba-1ae3-3608-a360-e967b02f5068 | -13.74122 | -60.12423 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 865c0346-4be6-3412-a70d-1b4928d5226a | -13.76549 | -60.56674 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29e03e04-41a2-3eb6-bf62-580b70a73209 | -13.75426 | -60.57297 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f4d5725-ba3b-30da-b1dd-2a28ceecfb72 | -13.75369 | -60.57668 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c5d7176-8e58-3196-b922-0648d80085a7 | -13.74467 | -60.12476 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb1c6139-b914-3f63-935c-0e5bb8370990 | -13.74066 | -60.12805 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea7348cc-04cb-3395-8cc0-d9f4c982f764 | -13.74352 | -60.59785 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ff357e2-5386-3e02-bc85-19e7d40188d5 | -13.73673 | -60.59678 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76807d5e-43b7-3ad5-b701-2a34400de17b | -13.76558 | -60.56716 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f9225ad8-2f5b-36cf-b284-8ed8181e2de3 | -13.76218 | -60.56662 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6fcf0cc-4f7d-3f08-95d1-72750f530c2e | -13.75879 | -60.56608 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b90570bd-0dc1-36d2-b26b-67e59b2ce312 | -13.74578 | -60.58302 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c6e0925-7bc2-315b-a5e7-e4f058e80608 | -13.74408 | -60.59415 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dfcd496-04bb-364a-9b74-2eff8d044580 | -13.74069 | -60.59361 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6e65e56e-de67-33ad-9400-5ed740c5d176 | -13.74012 | -60.59732 | 2024-10-12 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4be3518f-2b37-3090-8774-c5c8393ce532 | -15.62383 | -59.96317 | 2024-10-12 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c8369fc8-635e-3582-8921-2dee620c6511 | -3.70671 | -58.54507 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89f5b5f9-6e10-337f-8315-3e58d0ba254a | -3.70334 | -58.54454 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 816f6ea8-dab1-3eb2-9ea8-726da724d779 | -3.66606 | -58.80712 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f87d68e-a087-3b87-b748-cd2d7bb0dddb | -3.63784 | -58.62584 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ab9aecc-6b5d-325c-926c-0ac98d1e1daa | -3.53509 | -59.39044 | 2024-10-12 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3ad1d73-38b6-37ae-818a-a7c9231bcb5e | -3.48007 | -59.50231 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5489bb2e-db60-31f8-b01e-848dc77b15cc | -3.47952 | -59.50577 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56bad7a9-b663-3526-ad39-f04ff4e4a438 | -3.4762 | -59.50525 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README106.md)
