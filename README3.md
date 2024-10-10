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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee6e57da-9efc-357a-b30c-4381affc8376 | -9.0842 | -61.3925 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 3340386d-b33c-381f-83c8-ff3f0f9f4b7c | -9.0857 | -61.1629 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a99371c9-273c-3ad6-95af-4ccd6e3090ac | -9.0859 | -61.1437 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e76683ae-368e-31a0-8de0-d2c868c0faf0 | -9.1028 | -61.3917 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c29b43d3-a328-3606-8456-33fa309f6e4f | -9.1035 | -61.2769 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| cc8a60ad-ff79-3cf7-a01f-f096a0d5996f | -9.122 | -61.2951 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e1ed1a80-e124-30be-ad88-05156c88745a | -9.1221 | -61.276 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 2537f2a8-1a28-3a20-a83a-61337f2a2506 | -9.3548 | -48.8043 | 2024-10-10 00:15:59 | GOES-16 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 794ee3ff-0a2b-36c3-a8c4-9e629364459a | -9.3736 | -48.8025 | 2024-10-10 00:15:59 | GOES-16 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| c4ed2f6f-69f0-36c8-89bd-28db20e5c03c | -13.85809 | -42.43385 | 2024-10-10 00:16:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 5947bdab-e7f3-3f26-aa01-f25d55fc6535 | -11.89783 | -43.9029 | 2024-10-10 00:16:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 63bf8f89-478f-37e0-838f-fd862788ab6e | -11.89533 | -43.88196 | 2024-10-10 00:16:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 01c31d5c-2c26-3ccc-a8cd-a56563e97fed | -11.76586 | -44.56326 | 2024-10-10 00:16:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1f668d7a-da40-3957-9b24-2a37b25e89d0 | -11.53553 | -44.03592 | 2024-10-10 00:16:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| fd1ce392-4c0f-3e69-9089-cd822d05fc26 | -11.533 | -44.01466 | 2024-10-10 00:16:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 293b197e-c03d-3fc3-b6b2-6cc334dc7a6a | -11.53048 | -43.9935 | 2024-10-10 00:16:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| ce2fc92f-de38-3c96-a931-a999d88f43e9 | -11.52236 | -44.03749 | 2024-10-10 00:16:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 19108c44-0c6a-314a-9e7e-39bf16b783c5 | -11.51986 | -44.01632 | 2024-10-10 00:16:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 3d0a004b-c278-38fc-8065-0014aba822d6 | -11.51737 | -43.99517 | 2024-10-10 00:16:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e44d5b38-f9f7-34f4-b286-4a2df77da8a4 | -10.78914 | -44.34842 | 2024-10-10 00:16:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cd2a57d0-9fd8-32ba-aca4-baa46cc4231e | -10.77741 | -44.33285 | 2024-10-10 00:16:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 57aa2df1-2ce0-3b95-811e-4d991c714723 | -13.53071 | -44.33105 | 2024-10-10 00:16:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7359c2f6-bc94-3a7d-b51e-5f755d111c98 | -13.52811 | -44.30717 | 2024-10-10 00:16:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 2c6f081e-29d5-35e1-9449-d6aaed21ebef | -13.52211 | -44.31284 | 2024-10-10 00:16:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 62a3dbb8-2129-3b64-96f8-cef2bdfeeb18 | -13.51937 | -44.28925 | 2024-10-10 00:16:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| cf3d9aa0-7c59-3b90-8e10-6ffd72c1fced | -13.40446 | -44.70969 | 2024-10-10 00:16:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 6b389aa9-9f4a-3fc8-858f-25d03f7ba76a | -13.40168 | -44.68426 | 2024-10-10 00:16:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 7fe19bee-fef2-3f51-8012-4c8d44493cc4 | -13.39847 | -44.69019 | 2024-10-10 00:16:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 67c8decd-fbd7-3087-b18c-cf99eb23b9d2 | -12.36586 | -44.74198 | 2024-10-10 00:16:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 7390fee4-339a-3522-9d4d-9ce955abfc94 | -12.3616 | -44.74901 | 2024-10-10 00:16:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 57fdbf60-6978-3cd2-b7fb-b6794a232425 | -12.35874 | -44.72426 | 2024-10-10 00:16:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c0e119aa-8020-392b-816d-de2736d14eac | -12.28863 | -44.6076 | 2024-10-10 00:16:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 81607af6-69dd-39ce-8a29-d006fbb01a8b | -12.2783 | -44.39133 | 2024-10-10 00:16:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 3f2010c7-0821-34e3-aac4-d8acc862ca77 | -14.03488 | -44.02577 | 2024-10-10 00:16:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b0b0333b-dbc1-36dd-b067-29bd96ade9bc | -13.85554 | -44.54947 | 2024-10-10 00:16:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 1e1bf3f7-cb51-35b9-a1d9-0fbc96786683 | -13.84133 | -44.55116 | 2024-10-10 00:16:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| db5abc0a-7f4b-3bcb-923c-cebbd746ae99 | -13.80065 | -44.61489 | 2024-10-10 00:16:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| f6b32c54-e008-367f-9c9e-2669b395f068 | -10.60755 | -44.77955 | 2024-10-10 00:16:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 182d63ec-f8d4-375e-a08d-2f82bd1e2292 | -11.79125 | -47.3959 | 2024-10-10 00:16:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 720e8645-2197-326e-9a3e-4f4e912d399a | -11.78855 | -47.40313 | 2024-10-10 00:16:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 32c02768-ab7c-33d2-873a-52413aae57ae | -10.60099 | -47.72426 | 2024-10-10 00:16:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 27d9d694-137b-3ed5-9ab7-ddf71bde0b79 | -10.58214 | -48.06435 | 2024-10-10 00:16:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 06d604d4-4acc-3a34-8396-71b9ab5fe19e | -10.57739 | -48.01968 | 2024-10-10 00:16:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 12ba73df-d145-340c-a279-a362f59ec7d8 | -10.57706 | -48.02599 | 2024-10-10 00:16:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ff952aa9-7b22-3811-841a-a7b1adcd7fcd | -12.61443 | -39.62121 | 2024-10-10 00:16:00 | TERRA_M-M | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 2c94712b-dd58-3629-8ef2-ea94db5b380e | -12.20905 | -38.77509 | 2024-10-10 00:16:00 | TERRA_M-M | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 61b4c2ba-c2f3-3e65-893f-049a0bc0535d | -10.59171 | -37.11152 | 2024-10-10 00:16:00 | TERRA_M-M | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a17c8fd1-b158-3d29-878a-60a95cd123cd | -10.22473 | -36.34885 | 2024-10-10 00:16:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0b359851-8387-3946-a5ef-38e39b5f1020 | -10.22606 | -36.35809 | 2024-10-10 00:16:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 74ecc946-f555-351c-b4da-c0a63728cf48 | -9.38545 | -35.96054 | 2024-10-10 00:16:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c145453b-c54f-30f3-93a2-ee33da2855f2 | -9.614 | -35.88758 | 2024-10-10 00:16:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 91fceb8b-4692-3cf6-b3f9-d74ed7a278b8 | -9.90062 | -36.14864 | 2024-10-10 00:16:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.4 |
| 5a803f30-1380-3ab2-91e2-df2a1ec09516 | -9.90199 | -36.15808 | 2024-10-10 00:16:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 9ff7d644-5277-33d7-8eaf-7d16d67ee439 | -9.90969 | -36.14725 | 2024-10-10 00:16:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| 5445044f-6ca0-37ad-b022-b9b6c34f55fc | -9.91106 | -36.15668 | 2024-10-10 00:16:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.5 |
| 3bb6e3b0-e78d-32df-a44a-bd3b88f578d8 | -9.96887 | -36.30132 | 2024-10-10 00:16:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 3ee684bc-24ff-3b60-a66d-479b1719f098 | -9.97019 | -36.31055 | 2024-10-10 00:16:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| d759e900-b134-322b-8b76-3f0b3bba07ec | -10.2108 | -42.46012 | 2024-10-10 00:16:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 28e4985f-9108-3042-a77e-bfa937de0099 | -11.08917 | -41.54304 | 2024-10-10 00:16:00 | TERRA_M-M | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 61b01e05-4b06-3fff-9150-e30691eab3ae | -11.08226 | -41.53762 | 2024-10-10 00:16:00 | TERRA_M-M | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b7a786b0-b1cc-30e4-9a1c-41f75d25c09a | -13.31604 | -42.43002 | 2024-10-10 00:16:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| bae52d6d-9527-3b44-a3b9-aa101d1362d1 | -13.30987 | -42.43644 | 2024-10-10 00:16:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 7393a648-229e-33e5-9e5c-eba12bb782bc | -9.9136 | -36.1551 | 2024-10-10 00:16:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 0f8c0feb-3789-360c-a38e-f4f5b43a99fe | -9.9105 | -58.1313 | 2024-10-10 00:16:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| dc67702f-f593-35a5-9790-7974d7eed9df | -10.3707 | -61.2513 | 2024-10-10 00:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 29f2b8b7-984c-386c-807e-a26302a08521 | -10.3708 | -61.232 | 2024-10-10 00:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 20b5cb5e-bfd1-3860-b87e-988816817175 | -10.3894 | -61.2502 | 2024-10-10 00:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5d741a9f-6e72-3683-b65f-3b87588217a2 | -10.4287 | -60.9979 | 2024-10-10 00:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4540b038-7f87-37f6-b370-5eceda78b346 | -10.5746 | -48.0178 | 2024-10-10 00:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a8d70cbd-0a6b-39da-ac53-8ed61b36ccc8 | -11.0252 | -57.2436 | 2024-10-10 00:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 07b49632-9c6f-34d4-8de0-89aab06fcd35 | -11.0254 | -57.2237 | 2024-10-10 00:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 239.1 |
| 71772616-b31e-3e09-97cc-3f1dee657d4e | -11.0256 | -57.2038 | 2024-10-10 00:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 253.6 |
| 854c03f1-551b-3c43-b245-6c42d384e1a6 | -11.0443 | -57.2222 | 2024-10-10 00:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 298.8 |
| c173f877-7a81-3a3a-9adc-09e1895b347a | -11.0445 | -57.2023 | 2024-10-10 00:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 292.5 |
| 4446f6e4-ea7c-36b7-9cf6-84f257396695 | -11.2575 | -60.4855 | 2024-10-10 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| de409468-5145-34cb-85d5-aa0ac65c58f3 | -11.2582 | -60.4079 | 2024-10-10 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 05a3e504-3198-3c11-853f-ce5ddbf420a0 | -11.2583 | -60.3885 | 2024-10-10 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| aee3eb25-ad7a-310e-b7e5-c934dc840c6b | -11.2763 | -60.4844 | 2024-10-10 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fb02478f-6515-3657-b08e-3d350d2c1dff | -11.277 | -60.4067 | 2024-10-10 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c0ff1843-1f4a-3057-a7e6-f4903c5248ca | -11.2771 | -60.3873 | 2024-10-10 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 28ceef6a-2e93-385d-aaff-eb54622faa41 | -12.1955 | -46.7396 | 2024-10-10 00:16:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ad747293-1e19-3b6e-81bd-022a04e56b75 | -12.1958 | -46.717 | 2024-10-10 00:16:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7b9c277e-a504-350e-81f6-1c42d024476c | -12.2147 | -46.7369 | 2024-10-10 00:16:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 707a74ff-e9e1-3c11-ae90-182c1baac982 | -12.215 | -46.7143 | 2024-10-10 00:16:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 0dbb4b0a-dac0-3d5e-bcaa-d5d5590c24dd | -12.663 | -54.7193 | 2024-10-10 00:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| f3333881-5bcc-3ea4-a1c9-4eafbe259233 | -12.7244 | -63.0787 | 2024-10-10 00:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1b49fde4-cd1a-356f-93b6-a292a6bb0bf7 | -12.7245 | -63.0595 | 2024-10-10 00:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2619ecae-dc29-3dea-aa0d-dfdfa45ac338 | -13.5321 | -44.3173 | 2024-10-10 00:16:22 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8aa5ac93-6a09-3e68-acf3-f64cd89f304d | -13.5326 | -44.2937 | 2024-10-10 00:16:22 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| aa6bf060-af6b-3846-83f6-5362f0ba678f | -13.8184 | -44.5254 | 2024-10-10 00:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6625898b-56b0-37c7-b9c5-2382cc3994b5 | -13.8374 | -44.5455 | 2024-10-10 00:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 96021007-2c1b-3acc-9c8f-dedbb6249556 | -13.8379 | -44.522 | 2024-10-10 00:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| e3e8f179-cbb8-3564-a0b6-c57fd7b99b07 | -13.8569 | -44.5421 | 2024-10-10 00:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| c7ac13b3-fafa-3914-ae8c-a2b47b866fcf | -13.8574 | -44.5185 | 2024-10-10 00:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 82f1b690-4594-3b3c-a607-524b732026a3 | -13.8579 | -44.4949 | 2024-10-10 00:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6db02968-b44b-3aa5-aae9-8fc2fadb9bf3 | -14.0425 | -44.0367 | 2024-10-10 00:16:25 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 7ef11a8f-fd67-3ce3-aa17-737a26dc154d | -14.043 | -44.0129 | 2024-10-10 00:16:25 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1bf07fe8-fde7-35b9-850b-56682c284c4c | -20.569799 | -45.882301 | 2024-10-10 00:16:44 | METOP-C | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c644ebfb-d039-3d4b-a4df-666ed540bac7 | -20.560101 | -45.884201 | 2024-10-10 00:16:44 | METOP-C | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3f5f763a-75e8-3511-ba75-d3f324c9ded7 | -20.562901 | -45.900101 | 2024-10-10 00:16:44 | METOP-C | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
